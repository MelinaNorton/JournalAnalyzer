from langchain.schema import Document
from typing import List, Dict
import fitz
import re 
import json
from pathlib import Path
from langchain.text_splitter import TokenTextSplitter
import os
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
load_dotenv()

llm = ChatOpenAI(
        model_name="gpt-4.1",     
        temperature=0.0,        
        max_tokens=512,         
    )

#function that recieved a journal's PDF and extracts the raw text into a varible & returns it
def readpdf(path:str)->str:
    pdftext = []
    doc = fitz.open(path)
    for page in doc:
        temp = page.get_text()
        pdftext.append(temp);
    #return the variable "rawtext"
    doc.close()
    return "\n".join(pdftext)

#function that takes a journal's extracted data and formats it into a document with it's important properties (metadata)
#(as defined by the user in the Dictionary-template)
def gettemplate()->Dict[str, str]:
    getting = True
    template : Dict[str,str] = {}
    print("To finish creating the template, type D or d")
    while(getting):
        curr_key = input("Enter desired key:\n")
        curr_val = input("Enter desired value:\n")
        answer = input("Does this look correct?(y/n): key: " + curr_key + " value: " + curr_val + "\n")
        if(answer.lower()=='y'):
            template[curr_key] = curr_val
        elif(answer.lower()=='d'):
            getting = False
        else:
            continue    
    return template

#function from which the other above two are called; a list of journals is iterated through, parsed & formatted
#into documents then returned
def aggregatedata(journalspath:Path)->List[str]:
    filedatas : List[str] = []
    for file in journalspath.glob("*.pdf"):
        currfile_data = readpdf(file)
        filedatas.append(currfile_data)
    return filedatas

#split the passed-in raw document-metadata pair into a ~1000 token Document & return
def createembeddings(journaldatas:List[str])->List[List[str]]:
    textsplitter = TokenTextSplitter(encoding_name="cl100k_base", chunk_size=50, chunk_overlap=0)
    tokenized_journals : List[List[str]] = []
    for journaldata in journaldatas:
        currtokens = textsplitter.split_text(journaldata)
        tokenized_journals.append(currtokens)
    return tokenized_journals

def buildquery()->PromptTemplate:
    prompt = PromptTemplate(
        input_variables=["template", "journalcontexts"],
        template="""
            Reserach labs that deal with computational modeling often have to match journals particularly in order to ensure
            the integrity of their product. Knowing this, analyze the data from the provided journals and, based on the reseracher's
            desired attributes, choose a journal that is most likley to be worth reading/pursuing in the vetting process.

            Desired attributes:
            {template}

            Journal content:
            {journalcontexts}
        """
    )
    return prompt



def queryLLM(prompt:PromptTemplate, templatestr:str, journalcontexts:List[List[str]])->str:
    journal_context_str = "\n\n".join(chunk for journal in journalcontexts for chunk in journal)
    chain = LLMChain(llm=llm, prompt=prompt)
    answer = chain.run(
        template = templatestr,
        journalcontexts = journal_context_str
    )
    return answer
def compressjournals(filedatas:List[str])->List[str]:
    summarized_journals: List[str] = []

    prompt = PromptTemplate(
        input_variables=["journalcontext"],
        template="""
            Reserach labs that deal with computational modeling often have to match journals particularly in order to ensure
            the integrity of their product. Knowing this, analyze the data from the provided journals and, based on the reseracher's
            desired attributes, choose a journal that is most likley to be worth reading/pursuing in the vetting process. Before I later 
            send a query with all the journals, return a summary of this journal's full text that cuts out unecessary information/
            verbosity so as to not overwhelm the LLM with tokens. Make sure to include the journal name/author for identification

            Journal content:
            {journalcontext}
        """
    )
    for file in filedatas:
        journalcontext = file
        chain = LLMChain(llm=llm, prompt=prompt)
        answer = chain.run(
            journalcontext = journalcontext
        )
        summarized_journals.append(answer)
    return summarized_journals


here = Path(__file__).resolve().parent
project_root = here.parents[1]   
resources_path = project_root / "project" / "resources"
filedatas = aggregatedata(resources_path)
summarized_files = compressjournals(filedatas)
tokenizedjournals = createembeddings(summarized_files)
template = gettemplate()
templatestr = json.dumps(template, indent=2)
prompt = buildquery()
answer = queryLLM(prompt, templatestr, tokenizedjournals)
print(answer)



