import pymupdf
from langchain.schema import Document
from typing import List, Dict

#function that recieved a journal's PDF and extracts the raw text into a varible & returns it
def readpdf(path:str)->str:
    temp = 'temptext'
    #read data into a variable "rawtext" from the filepath using get_text()
    #return the variable "rawtext"
    return temp

#split the passed-in raw document-metadata pair into a ~1000 token Document & return
def createembeddings(doc:Document, metadata: Dict[str,str])->List[List[float]]:
    temp = 'temptext'
    return temp

#function that takes a journal's extracted data and formats it into a document with it's important properties (metadata)
#(as defined by the user in the Dictionary-template)
def printreport(text:str, metadata:Dict[str, str])->Document:
    temp = 'temptext'
    #using find() and find_all(), populate the fields as found in the metadata-template into a Dict[str, str]
    #build a new Document variable, with the text being "text" and the metadata being this new Dict
    #return
    return temp

#function from which the other above two are called; a list of journals is iterated through, parsed & formatted
#into documents then returned
def aggregatedata(journals:List[str], metadatas:List[Dict[str,str]])->List[Document]:
    temp = 'temptext'
    return temp

#recieve user input for the query
def getquery()->None:
    temp = 'temptext'

def queryLLMEmbeddings(embeddings:List[float], query:str)->str:
    temp = 'temptext'
    return temp
