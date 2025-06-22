from langchain.schema import Document
from typing import List, Dict
import fitz
import re 
from pathlib import Path
from langchain.text_splitter import TokenTextSplitter
import os
from langchain import OpenAI
from dotenv import load_dotenv, find_dotenv


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
    print("To finish creating the template, type N or n")
    while(getting):
        curr_key = input("Enter desired key")
        curr_val = input("Enter desired value")
        answer = input("Does this look correct?(y/n): key: " + curr_key + " value: " + curr_val)
        if(answer.lower()=='y'):
            template[curr_key] = curr_val
        elif(answer.lower()=='n'):
            getting = False
        else:
            continue    
    return template

#function from which the other above two are called; a list of journals is iterated through, parsed & formatted
#into documents then returned
def aggregatedata(journalspath:str)->List[str]:
    for file in resources_path.glob("*.pdf"):
        currfile_data = readpdf(file)
        filedatas.append(currfile_data)

#split the passed-in raw document-metadata pair into a ~1000 token Document & return
def createembeddings(journaldatas:List[str])->List[List[str]]:
    textsplitter = TokenTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0)
    tokenized_journals : List[List[str]] = []
    for journaldata in journaldatas:
        currtokens = textsplitter.split_text(journaldata)
        tokenized_journals.append(currtokens)
    return tokenized_journals

def queryLLM(embeddings:List[float], template:List[str], query:str)->str:
    
    temp = 'temptext'
    return temp

here = Path(__file__).resolve().parent
project_root = here.parents[1]   
resources_path = project_root / "project" / "resources"
filedatas = aggregatedata(resources_path)
tokenizedjournals = createembeddings(filedatas)
template = gettemplate()

