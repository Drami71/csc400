from pyzotero import zotero
import pprint
import pandas as pd
import time
import crossref_commons.retrieval
from crossref_commons.retrieval import get_entity
from crossref_commons.types import EntityType, OutputType

zot = zotero.Zotero('','user','')
def book_chapter(bookchapter_dictionary):
    bookchapter_template = zot.item_template('book')
    try:    
        bookchapter_template['ISBN'] = bookchapter_dictionary['ISBN']
    except:
        bookchapter_template['ISBN'] = ''
    try:
        bookchapter_template['abstractNote'] = bookchapter_dictionary['abstractNote']
    except:
        bookchapter_template['abstractNote'] = ''
    try:
        bookchapter_template['accessDate'] = bookchapter_dictionary['accessDate']
    except:
        bookchapter_template['accessDate'] = ''
    try:
        bookchapter_template['archive'] = bookchapter_dictionary['archive']
    except:
        bookchapter_template['archive'] = ''
    try:
        bookchapter_template['archiveLocation'] = bookchapter_dictionary['archiveLocation']
    except:
        bookchapter_template['archiveLocation'] = ''
    try:
        bookchapter_template['callNumber'] = bookchapter_dictionary['callNumber']
    except:
        bookchapter_template['callNumber'] = ''
    try:
        bookchapter_template['collections'] = bookchapter_dictionary['collections']
    except:
        bookchapter_template['collections'] = []
    try:
        bookchapter_template['creators'] = [{'creatorType': 'author', 
                                  'firstName': [d['given'] for d in bookchapter_dictionary['author']][0], 
                                  'lastName': [d['family'] for d in bookchapter_dictionary['author']][0]}]
    except:
        bookchapter_template['creators'] = [{'creatorType': 'author', 
                                                'firstName': '', 
                                                'lastName': ''}]    
    try:
        bookchapter_template['date'] = bookchapter_dictionary['created']['date-parts'][0][0]
    except:
        bookchapter_template['date'] = ''
    try:
        bookchapter_template['edition'] = bookchapter_dictionary['edition']
    except:
        bookchapter_template['edition'] = ''
    try:
        bookchapter_template['extra'] = bookchapter_dictionary['extra']
    except:
        bookchapter_template['extra'] = ''
        
    bookchapter_template['itemType'] = 'book'
    
    try:
        bookchapter_template['language'] = bookchapter_dictionary['language']
    except:
        bookchapter_template['language'] = ''
    try:
        bookchapter_template['libraryCatalog'] = bookchapter_dictionary['libraryCatalog']
    except:
        bookchapter_template['libraryCatalog'] = ''
    try:
        bookchapter_template['numPages'] = bookchapter_dictionary['numPages']
    except:
        bookchapter_template['numPages'] = ''
    try:
        bookchapter_template['numberOfVolumes'] = bookchapter_dictionary['numberOfVolumes']
    except:
        bookchapter_template['numberOfVolumes'] = ''
    try:
        bookchapter_template['place'] = bookchapter_dictionary['place']
    except:
        bookchapter_template['place'] = ''
    try:
        bookchapter_template['publisher'] = bookchapter_dictionary['publisher']
    except:
        bookchapter_template['publisher'] = ''
    try:
        bookchapter_template['relations'] = bookchapter_dictionary['relation']
    except:
        bookchapter_template['relations'] = {}
    try:
        bookchapter_template['rights'] = bookchapter_dictionary['rights']
    except:
        bookchapter_template['rights'] = ''
    try:
        bookchapter_template['series'] = bookchapter_dictionary['series']
    except:
        bookchapter_template['series'] = ''
    try:
        bookchapter_template['seriesNumber'] = bookchapter_dictionary['seriesNumber']
    except:
        bookchapter_template['seriesNumber'] = ''
    try:
        bookchapter_template['shortTitle'] = bookchapter_dictionary['shortTitle']
    except:
        bookchapter_template['shortTitle'] = ''
    try:
        bookchapter_template['tags'] = bookchapter_dictionary['tags']
    except:
        bookchapter_template['tags'] = []
    try:
        bookchapter_template['title'] = bookchapter_dictionary['title'][0]
    except:
        bookchapter_template['title'] - ''
    try:
        bookchapter_template['url'] = bookchapter_dictionary['URL']
    except:
        bookchapter_template['url'] = ''
    try:
        bookchapter_template['volume'] = bookchapter_dictionary['volume']
    except:
        bookchapter_template['volume'] = ''
    resp = zot.create_items([bookchapter_template])
    #pprint.pprint(resp)
    print("Populated: ",bookchapter_dictionary['title'][0])
    
def book(book_dictionary):
    pprint.pprint(book_dictionary)
    book_template = zot.item_template('book')
    try:    
        book_template['ISBN'] = book_dictionary['ISBN']
    except:
        book_template['ISBN'] = ''
    try:
        book_template['abstractNote'] = book_dictionary['abstractNote']
    except:
        book_template['abstractNote'] = ''
    try:
        book_template['accessDate'] = book_dictionary['accessDate']
    except:
        book_template['accessDate'] = ''
    try:
        book_template['archive'] = book_dictionary['archive']
    except:
        book_template['archive'] = ''
    try:
        book_template['archiveLocation'] = book_dictionary['archiveLocation']
    except:
        book_template['archiveLocation'] = ''
    try:
        book_template['callNumber'] = book_dictionary['callNumber']
    except:
        book_template['callNumber'] = ''
    try:
        book_template['collections'] = book_dictionary['collections']
    except:
        book_template['collections'] = []
    try:
        book_template['creators'] = [{'creatorType': 'author', 
                                  'firstName': [d['given'] for d in book_dictionary['author']][0], 
                                  'lastName': [d['family'] for d in book_dictionary['author']][0]}]
    except:
        book_template['creators'] = [{'creatorType': 'author', 
                                                'firstName': '', 
                                                'lastName': ''}]    
    try:
        book_template['date'] = book_dictionary['created']['date-parts'][0][0]
    except:
        book_template['date'] = ''
    try:
        book_template['edition'] = book_dictionary['edition']
    except:
        book_template['edition'] = ''
    try:
        book_template['extra'] = book_dictionary['extra']
    except:
        book_template['extra'] = ''
        
    book_template['itemType'] = 'book'
    
    try:
        book_template['language'] = book_dictionary['language']
    except:
        book_template['language'] = ''
    try:
        book_template['libraryCatalog'] = book_dictionary['libraryCatalog']
    except:
        book_template['libraryCatalog'] = ''
    try:
        book_template['numPages'] = book_dictionary['numPages']
    except:
        book_template['numPages'] = ''
    try:
        book_template['numberOfVolumes'] = book_dictionary['numberOfVolumes']
    except:
        book_template['numberOfVolumes'] = ''
    try:
        book_template['place'] = book_dictionary['place']
    except:
        book_template['place'] = ''
    try:
        book_template['publisher'] = book_dictionary['publisher']
    except:
        book_template['publisher'] = ''
    try:
        book_template['relations'] = book_dictionary['relation']
    except:
        book_template['relations'] = {}
    try:
        book_template['rights'] = book_dictionary['rights']
    except:
        book_template['rights'] = ''
    try:
        book_template['series'] = book_dictionary['series']
    except:
        book_template['series'] = ''
    try:
        book_template['seriesNumber'] = book_dictionary['seriesNumber']
    except:
        book_template['seriesNumber'] = ''
    try:
        book_template['shortTitle'] = book_dictionary['shortTitle']
    except:
        book_template['shortTitle'] = ''
    try:
        book_template['tags'] = book_dictionary['tags']
    except:
        book_template['tags'] = []
    try:
        book_template['title'] = book_dictionary['title'][0]
    except:
        book_template['title'] - ''
    try:
        book_template['url'] = book_dictionary['URL']
    except:
        book_template['url'] = ''
    try:
        book_template['volume'] = book_dictionary['volume']
    except:
        book_template['volume'] = ''

    resp = zot.create_items([book_template])
    pprint.pprint(resp)
    print("Populated: ",book_dictionary['title'][0])


def journal(journal_dictionary):
    journalArticle_template = zot.item_template('journalArticle')
    try:
        journalArticle_template['DOI'] = journal_dictionary['DOI']
    except:
        journalArticle_template['DOI'] = ''
    try: 
        journalArticle_template['ISSN'] = journal_dictionary['ISSN'][0]
    except:
        journalArticle_template['ISSN'] = ''
    try:
        journalArticle_template['abstractNote'] = journal_dictionary['abstractNote']
    except:
        journalArticle_template['abstractNote'] = ''
    try:
        journalArticle_template['accessDate']  = journal_dictionary['accessDate']
    except:
        journalArticle_template['accessDate'] = ''
    try:
        journalArticle_template['archive'] = journal_dictionary['archive']
    except:
        journalArticle_template['archive'] = ''   
    try:
        journalArticle_template['archiveLocation'] = journal_dictionary['archiveLocation']
    except:
         journalArticle_template['archiveLocation'] = ''
    try:
        journalArticle_template['callNumber'] = journal_dictionary['callNumber']
    except:
         journalArticle_template['callNumber'] = ''
    try:
        journalArticle_template['collections'] = journal_dictionary['collections']
    except:
         journalArticle_template['collections'] = []  
    try:
        journalArticle_template['creators'] =  [{'creatorType': 'author', 
                                                'firstName': [d['given'] for d in journal_dictionary['author']][0], 
                                                'lastName': [d['family'] for d in journal_dictionary['author']][0]}]
    except:
         journalArticle_template['creators'] = [{'creatorType': 'author', 
                                                'firstName': '', 
                                                'lastName': ''}]    
    try:
        journalArticle_template['date'] = journal_dictionary['created']['date-parts'][0][0]
    except:
         journalArticle_template['date'] = ''
    try:
        journalArticle_template['extra'] = journal_dictionary['extra']
    except:
         journalArticle_template['extra'] = ''      
    try:
        journalArticle_template['issue'] = journal_dictionary['issue']
    except:
         journalArticle_template['issue'] = ''    
    
    journalArticle_template['itemType'] = 'journalArticle'
     
    try:
        journalArticle_template['journalAbbreviation'] = journal_dictionary['journalAbbreviation']
    except:
         journalArticle_template['journalAbbreviation'] = ''      
    try:
        journalArticle_template['language'] = journal_dictionary['language']
    except:
         journalArticle_template['language'] = ''     
        
    try:
        journalArticle_template['libraryCatalog'] = journal_dictionary['libraryCatalog']
    except:
         journalArticle_template['libraryCatalog'] = ''       
    try:
        journalArticle_template['pages'] = journal_dictionary['page']
    except:
         journalArticle_template['pages'] = ''      
    try:
        journalArticle_template['publicationTitle'] = journal_dictionary['publisher']
    except:
         journalArticle_template['publicationTitle'] = ''    
    try:
        journalArticle_template['relations'] = journal_dictionary['relation']
    except:
         journalArticle_template['relations'] = {}       
    try:
        journalArticle_template['rights'] =  journal_dictionary['rights']
    except:
         journalArticle_template['rights'] = ''    
    try:
        journalArticle_template['series'] = journal_dictionary['series']
    except:
         journalArticle_template['series'] = ''  
    try:
        journalArticle_template['seriesText'] = journal_dictionary['seriesText']
    except:
         journalArticle_template['seriesText'] = ''    
    try:
        journalArticle_template['seriesTitle'] = journal_dictionary['seriesTitle']
    except:
         journalArticle_template['seriesTitle'] = ''     
    try:
        journalArticle_template['shortTitle'] = journal_dictionary['shortTitle'][0]
    except:
         journalArticle_template['shortTitle'] = '' 
    try:
        journalArticle_template['tags'] = journal_dictionary['tags']
    except:
         journalArticle_template['tags'] = []     
    try:
        journalArticle_template['title'] = journal_dictionary['title'][0]
    except:
         journalArticle_template['title'] = ''     
    try:
        journalArticle_template['url'] = journal_dictionary['URL']
    except:
         journalArticle_template['url'] = ''       
    try:
        journalArticle_template['volume'] = journal_dictionary['volume']
    except:
         journalArticle_template['volume'] = ''     
        
    resp = zot.create_items([journalArticle_template])
    print("Populated: ",journal_dictionary['title'][0])
    
def conference_paper(conference_dictionary):
    conferencePaper_template = zot.item_template('conferencePaper')
    try:
        conferencePaper_template['DOI'] = conference_dictionary['DOI']
    except:
        conferencePaper_template['DOI'] = ''
    try:
        conferencePaper_template['ISBN'] = conference_dictionary['ISBN']
    except:
        conferencePaper_template['ISBN'] = ''
    try:
        conferencePaper_template['abstractNote'] = conference_dictionary['abstractNote']
    except:
        conferencePaper_template['abstractNote'] = '' 
    try:
        conferencePaper_template['abstractDate'] = conference_dictionary['abstractDate']
    except:
        conferencePaper_template['accessDate'] = ''    
    try:
        conferencePaper_template['archive'] = conference_dictionary['archive']
    except:
        conferencePaper_template['archive'] = '' 
    try:
        conferencePaper_template['archiveLocation'] = conference_dictionary['archiveLocation']
    except:
        conferencePaper_template['archiveLocation'] = '' 
    try:
        conferencePaper_template['callNumber'] = conference_dictionary['callNumber']
    except:
        conferencePaper_template['callNumber'] = ''    
    try:
        conferencePaper_template['collections'] = conference_dictionary['collections']
    except:
        conferencePaper_template['collections'] = []      
    try:
        conferencePaper_template['creators'] =  [{'creatorType': 'author', 
                                                'firstName': [d['given'] for d in conference_dictionary['author']][0], 
                                                'lastName': [d['family'] for d in conference_dictionary['author']][0]}]
    except:
        conferencePaper_template['creators'] = [{'creatorType': 'author', 
                                                'firstName': '', 
                                                'lastName': ''}]          
    try:
        conferencePaper_template['date'] = conference_dictionary['created']['date-parts'][0][0]
    except:
        conferencePaper_template['date'] = ''        
    try:
        conferencePaper_template['extra'] = conference_dictionary['extra']
    except:
        conferencePaper_template['extra'] = ''      
        
        
    conferencePaper_template['itemType'] = 'conferencePaper'
    try:
        conferencePaper_template['language'] = conference_dictionary['language']
    except:
        conferencePaper_template['language'] = ''
    try:
        conferencePaper_template['libraryCatalog'] = conference_dictionary['libraryCatalog']
    except:
        conferencePaper_template['libraryCatalog'] = ''  
    try:
        conferencePaper_template['pages'] = conference_dictionary['pages']
    except:
        conferencePaper_template['pages'] = ''     
    try:
        conferencePaper_template['place'] = conference_dictionary['place']
    except:
        conferencePaper_template['place'] = ''      
    try:
        conferencePaper_template['proceedingsTitle'] = conference_dictionary['proceedingsTitle']
    except:
        conferencePaper_template['proceedingsTitle'] = ''      
    try:
        conferencePaper_template['publisher'] = conference_dictionary['publisher']
    except:
        conferencePaper_template['publisher'] = ''          
    try:
        conferencePaper_template['relations'] = conference_dictionary['relation']
    except:
        conferencePaper_template['relations'] = {}     
    try:
        conferencePaper_template['rights'] = conference_dictionary['rights']
    except:
        conferencePaper_template['rights'] = ''    
    try:
        conferencePaper_template['series'] = conference_dictionary['series']
    except:
        conferencePaper_template['series'] = ''        
    try:
        conferencePaper_template['shortTitle'] = conference_dictionary['shortTitle'][0]
    except:
        conferencePaper_template['shortTitle'] = ''        
    try:
        conferencePaper_template['tags'] = conference_dictionary['tags']
    except:
        conferencePaper_template['tags'] = []    
    try:
         conferencePaper_template['title'] = conference_dictionary['title'][0]
    except:
         conferencePaper_template['title'] = ''     
    try:
         conferencePaper_template['url'] = conference_dictionary['URL']
    except:
         conferencePaper_template['url'] = ''        
    try:
         conferencePaper_template['volume'] = conference_dictionary['volume']
    except:
         conferencePaper_template['volume'] = ''       
        
    resp = zot.create_items([conferencePaper_template])
    pprint.pprint(resp)
    print("Populated: ",conference_dictionary['title'][0])
    
def formatDict(unformatedDictionary):
    #second to last one is other, does not have way to go in
    #10.1002/9781118663219.wbegss266 is a book in Zotero, other in Crossref
    itemtype = unformatedDictionary['type']
    if("mml:math" in unformatedDictionary['title'][0]):
        print("Failed to populate: ",unformatedDictionary['title'][0]," Dis shit fucked")
    elif(itemtype == 'journal-article'):
        journal(unformatedDictionary)
    elif (itemtype == 'proceedings-article'):
        conference_paper(unformatedDictionary)
    elif(itemtype == 'book-chapter'):
        book_chapter(unformatedDictionary)
    elif(itemtype == 'book' or itemtype == 'monograph' or itemtype == 'edited-book'):
        book(unformatedDictionary)
    
    #elif(itemtype == 'unkown'):
    #    report(data)
    #elif(itemtype == 'unkown'):
    #    magazine(data)
    #elif(itemtype =='unknown'):
    #     presentation(data)
    # elif(itemtype =='dataset'):
    #    dataset(data)