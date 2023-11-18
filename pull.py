from pybliometrics.scopus.utils import config
from pybliometrics.scopus import AffiliationRetrieval, AffiliationSearch, ScopusSearch, AbstractRetrieval
import crossref_commons.retrieval
import pybliometrics
from crossref_commons.retrieval import get_entity
from crossref_commons.types import EntityType, OutputType
from pyzotero import zotero
import pprint
import pandas as pd
import time
from functions import *

{
  "User-Agent": "<<polite user agent; including: >",
  "": "<<>>"
}


query = "AFFIL(Southern Connecticut State University)"

southernAffils = AffiliationSearch(query)

southernAffils.affiliations

#print(southernAffils)

    



pd.set_option('display.max_columns', None)

#print(pd.DataFrame(s.affiliations))

#print(s)

s = ScopusSearch('AFFIL(Southern Connecticut State University)')
dfSCSU = pd.DataFrame(pd.DataFrame(s.results))
s = ScopusSearch('AFFIL(Connecticut State Colleges and Universities)')
dfCSCU = pd.DataFrame(pd.DataFrame(s.results))


#pd.set_option('display.max_columns', None)
#print(df.doi)

#for col in df.columns:
#   print(col)
    


#print(doiDf)
#print(df.iloc[[x],[1]])


#Creating the list of doi so that they can be added to respective dataframes wether they have a doi or no doi as ones with Doi's can be passed through crossref.
doiCol = dfSCSU['doi']
noDoiDF = pd.DataFrame(columns = dfSCSU.columns)
doiDF =pd.DataFrame(columns = dfSCSU.columns)


#searhes through all the doi's and added them to their respective dataframe the doi or non doi for the Southern Connecticut State University affiliation
start = time.time()
count = 0
for document in doiCol:
    if(document == None):
        noDoiDF = pd.concat([noDoiDF,dfSCSU.iloc[[count]]])
    else:
        doiDF = pd.concat([doiDF,dfSCSU.iloc[[count]]])
    count = count +1
end = time.time()
print("Runtime doiDF/noDoiDF for SCSU: ", end - start)
#searhes through all the doi's and added them to their respective dataframe the doi or non doi for the Connecticut State Colleges and Universities affiliation
start = time.time()
doiCol = dfCSCU['doi']
count = 0
for document in doiCol:
    if(document == None):
        noDoiDF = pd.concat([noDoiDF,dfCSCU.iloc[[count]]])
    else:
        doiDF = pd.concat([doiDF,dfCSCU.iloc[[count]]])
    count = count +1
end = time.time()
print("Runtime doiDF/noDoiDF for CSCU: ", end - start)
noDoiDF.drop_duplicates()
doiDF.drop_duplicates()

#print(len(noDoiDF))

doiCol = pd.Series(doiDF['doi'])
#print(doiCol)
#print(crossref_commons.retrieval.get_publication_as_json(doiCol[0]))

crossRefDictionary = []
#doiCol.drop([0])

#print(doiDF)
#print(noDoiDF)

nameCol = pd.Series(doiDF['description'])
#for name in nameCol:
#    print(name)

#crossRefTypeList=[]
crossRefDictionaryList = []
crossRefBadList = []
count =0

start = time.time()
for doi in doiCol:
    if count <=150: #remove this
                #print(count)
            #print(doi)
        try:
            data = get_entity(doi,EntityType.PUBLICATION,OutputType.JSON)
            crossRefDictionaryList.append(data)
            #pprint.pprint(data)
            #print(crossRefDictionaryList)
            #print(data['DOI'])
            #print("success")
            tempE = data
            #print(type(tempE))
            checkValue = tempE['type']
            #containsV = False
            #for types in crossRefTypeList:
            #    if checkValue == types:
            #        containsV = True
            #if containsV == False:
            #    crossRefTypeList.append(checkValue)
            #    print("added value: ", checkValue)       
        except:
            crossRefBadList.append(doi)
            noDoiDF = pd.concat([noDoiDF,doiDF.iloc[count]])
            #print("fail")
        #print(get_entity(doi,EntityType.PUBLICATION,OutputType.JSON))
        count +=1
    #print(crossRefDictionaryList[0])
    #print(crossRefDictionaryList)
    #print("Cross ref done")
    #there are 25 of these currently
    #print(len(crossRefBadList))
end = time.time()
print("Runtime crossRefDictionaryList: ", end - start)

#for items in crossRefTypeList:
#    print("Types in CrossRef: ", items)


"""
for x in range(0,50):
    d = crossRefDictionaryList[x]['data']
    #print(d)
    pprint.pprint(d)
    #print()
    my_list = [i for i in d.values()]
    tempDoi = my_list[16]
    #if(tempDoi != "" and tempDoi != "en" and tempDoi != "English"):
        #zotDoiList.append(tempDoi)
        #print(tempDoi)
    #print(item)
    pprint.pprint(d)
    #print(type(d))
    #print(d['date'])"""


start = time.time()
zot = zotero.Zotero('4421509','group','YWq3eh8BBDE9adJY66lDvrzd')
items = zot.everything(zot.top()) #final line
#items = zot.top(limit=10)
end = time.time()
print("items Creation Runtime: ", end - start)


# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
zotTypeList = []
#item types wanted are 
start = time.time()
zotDoiList = []
for item in items:
    #print(item)
    d = item['data']
    #print(d)
    #pprint.pprint(d)
    #print()
    my_list = [i for i in d.values()]
    #print(my_list[3])
    tempName = d['title']
    #tempValue = d['itemType']
    #print(tempName)
    #containsV = False
    #for types in zotTypeList:
    #    if tempValue == types:
    #        containsV = True
            
    #if containsV == False:
    #    zotTypeList.append(tempValue)
        #print("zot value type: ", tempValue)
        
        
    #if(tempName != "" and tempName != "en" and tempName != "English"):
        #print(tempDoi)
    zotDoiList.append(tempName)
        #print(tempDoi)
    
    #print(item)
    #pprint.pprint(d)
    #print(type(d))
    #print(d['date'])
    #print(item['data']['doi'])
end = time.time()
print("Runtime zotDoiList Creation: ", end - start)


for types in zotTypeList:
    print("Zot type: ", types)

#checkValue = tempE['type']

addZotList = []
startOuter = time.time()
inputDoiLen = len(crossRefDictionaryList)
for n in range(0,inputDoiLen):
    startInner = time.time()
    tempE = crossRefDictionaryList[n]
    #print(type(tempE))
    try:
        tempName = tempE['title'][0]
        passName = True
    except:
        passName = False
    #print(tempName)
     
    for zDoi in zotDoiList:
        #print("CrossRef: ",tempDoi, " comparing to ", "Zotero: ", zDoi)
        if tempName == zDoi:
            passName = False
    if (passName == True) and (not("mml:math" in tempName)):
        addZotList.append(crossRefDictionaryList[n])
        endInner = time.time()
        print("Runtime doi compare: ", tempName, ", Time: ",endInner - start, ", Result: Pass")
    else:
        endInner = time.time()
        print("Runtime doi compare: ", tempName, ", Time: ",endInner - start, ", Result: Fail")
endOuter = time.time()
print("Runtime addZotList: ", endOuter - startOuter)
print("Num of Data from CrossRef to Populate into Zotero: ", len(addZotList))

#this populates into database dont use this unless its for realsies
#print(zot.item_types())
#pprint.pprint(zot.item_creator_types('artwork'))
#pprint.pprint(zot.item_template('journalArticle'))
#pprint.pprint(zot.item_creator_types('audioRecording'))
for item in addZotList:
    start = time.time()
    formatDict(item)
    end = time.time()
    #print("Added item: ", item['title'][0], ", Time: ",end - start)
    
"""

To format
Zot type:  journalArticle,  in crossRef: journal-article
Zot type:  conferencePaper,  in crossRef: proceedings-article
Zot type:  bookSection,  in crossRef:  book-chapter
Zot type:  book,  in crossRef: book, monograph, edited-book
Zot type:  report,  in crossRef: unkn
Zot type:  magazineArticle,  in crossRef: unkn
Zot type:  presentation,  in crossRef: unkn
dataset == {'itemType': 'dataset', 'localized': 'Dataset'}

{'DOI': '',
 'ISSN': '',
 'abstractNote': '',
 'accessDate': '',
 'archive': '',
 'archiveLocation': '',
 'callNumber': '',
 'collections': [],
 'creators': [{'creatorType': 'author', 'firstName': '', 'lastName': ''}],
 'date': '',
 'extra': '',
 'issue': '',
 'itemType': 'journalArticle',
 'journalAbbreviation': '',
 'language': '',
 'libraryCatalog': '',
 'pages': '',
 'publicationTitle': '',
 'relations': {},
 'rights': '',
 'series': '',
 'seriesText': '',
 'seriesTitle': '',
 'shortTitle': '',
 'tags': [],
 'title': '',
 'url': '',
 'volume': ''}

"""