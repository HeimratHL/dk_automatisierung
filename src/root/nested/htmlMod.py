# -*- coding: utf-8 -*-
'''
Created on 27.11.2018

@author: Anton

@note: I've stored the codesnippets in seperate textfile found in strpath. Building a HTML page by this works by reading the snippets, inserting parameters like the price of an entry,
then  finding the appropriate code placeholder in the template and inserting the snippet at the given lineindex.
'''

import os, subprocess
from tkinter.constants import ACTIVE

#Important Filepaths
strpath = os.path.join('D:\\', 'Desktop', 'pyfolder')
firefoxPath = os.path.join('C:\\', 'Program Files', 'Mozilla Firefox', 'firefox.exe')

#Caches the placeholder strings inside the snippets
cTemplate = "<!--code_template17040512773411457715-->"
cNewPage = "<!--code_newPage05565400559591493791-->"
cNewColumn = "<!--code_newColumn99082008157953769982-->"
cNewTable = "<!--code_newTable88824758446917230372-->"
gifNewPage = "<!--gif-name42400233872280850289-->"
titleNewPage = "<!--pagetitle22889233202272493537-->"
nameNewTable = "<!--table-name54845187244651894351-->"
titleNewEntry = "<!--entry-title69268835613672992291-->"
subtitleNewEntry = "<!--subtitle20695851250842941751-->"
sizeNewEntry = "<!--entry-size32101880553337566628-->"
priceNewEntry = "<!--entry-price45117288500038563995-->"

#Other variables
doubleNewLine = ["\n", "\n"]    

#Method to filter out characters that HTML isn't familiar with
def umlaut(zeile):
    text = ''
    string = str(zeile)
    for zeichen in string:
        if zeichen == u'ä':
            text += '&auml;'
        elif zeichen == u'ö':
            text += '&ouml;'
        elif zeichen == u'ü':
            text += '&uuml;'
        elif zeichen == u'ß':
            text += '&szlig;'
        elif zeichen == u'Ä':
            text += '&Auml;'
        elif zeichen == u'Ö':
            text += '&Ouml;'
        elif zeichen == u'Ü':
            text += '&Uuml;'
        elif zeichen == u'€':
            text += '&euro;'
        elif zeichen == u'&':
            text += '&amp;'
        elif zeichen == u'<':
            text += '&lt;'
        elif zeichen == u'>':
            text += '&rt;'
        elif zeichen == u'§':
            text += '&sect;'
        else:
            text += zeichen
    return text

#Method to remove existing templates
def removeTemplate(templateName):
    filename = templateName + ".html"
    filepath = os.path.join(strpath, filename)
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        os.remove(filepath)
        print("Template " + templateName + " removed!")

#Method to create a new template. The name is needed for further snippet adding
def newTemplate(templateName):
    
    filename = templateName + ".html"
    filepath = os.path.join(strpath, filename)
    
    if os.path.isfile(filepath):
        print("File/Folder already exists!")
    else:
        #copy the content of template.html to name.html
        file = open(os.path.join(strpath, 'template.html'), "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(filepath), "w")
        file.writelines(content)
        file.close()
        
        print("New template " + templateName + " created!")

#Method to create a new page in a given template
def newPage(templateName,gifName,title):
    
    templateFilename = templateName + ".html"
    filepath = os.path.join(strpath,templateFilename)
    
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        file = open(filepath, "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(strpath, 'newPage.html'), "r")
        snippet = file.readlines()
        file.close()
        
        #get infos about the snipet-parameter and their placements. This process makes it easy to edit the snippet file later as long as the placeholder remains the same.
        lensnippet = int(len(snippet))
        indexGif = [x for x in range(lensnippet) if gifNewPage in snippet[x].lower()]
        intIndexGif = int(indexGif[0])
        strGif = '\n         <section data-background="assets/' + gifName + '">'
        indexTitle = [x for x in range(lensnippet) if titleNewPage in snippet[x].lower()]
        intIndexTitle = int(indexTitle[0])
        strTitle = '\n          <h2>' + title + '</h2>\n'
        
        #insert the paramaters into snippet
        snippet[intIndexGif] = strGif
        snippet[intIndexTitle] = strTitle

        #get index of codeplacement and place snippet in content[indexC]
        indexC = -1
        for i in content:
            indexC = indexC + 1
            if cTemplate in i:
                break
               
        a = content[0:indexC]
        b = content[indexC:int(len(content))]
        content = a + doubleNewLine + snippet + doubleNewLine + b
        
        #write the new html file
        file = open(filepath, "w")
        file.writelines(content)
        file.close()
        
        print("Added new page to template " + templateName)
        
        
#Method to create a new column in a given page
def newColumn(templateName):
    
    templateFilename = templateName + ".html"
    filepath = os.path.join(strpath,templateFilename)
    
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        file = open(filepath, "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(strpath, 'newColumn.html'), "r")
        snippet = file.readlines()
        file.close()
                
        #get index of codeplacement and place snippet in content[indexC]
        indexC = -1
        for i in content:
            indexC = indexC + 1
            if cNewPage in i:
                break
               
        a = content[0:indexC]
        b = content[indexC:int(len(content))]
        content = a + doubleNewLine + snippet + doubleNewLine + b
        
        #write the new html file
        file = open(filepath, "w")
        file.writelines(content)
        file.close()

        print("Added new column to template " + templateName)


#Method to create a new table in a given column or page
def newTable(templateName,tableName):
    
    templateFilename = templateName + ".html"
    filepath = os.path.join(strpath,templateFilename)
    
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        file = open(filepath, "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(strpath, 'newTable.html'), "r")
        snippet = file.readlines()
        file.close()
        
        #get infos about the snippet-parameter and their placements. This process makes it easy to edit the snippet file later as long as the placeholder remains the same.
        indexName = -1
        for i in snippet:
            indexName = indexName + 1
            if nameNewTable in i:
                break
               
        strName = '                <thead><tr><td colspan="3">' + tableName + '</td></tr></thead>'
        
        #insert the paramaters into snippet
        snippet[indexName] = strName

        #get index of codeplacement and place snippet in content[indexC]
        indexC = -1
        for i in content:
            indexC = indexC + 1
            if cNewColumn in i:
                break
               
        a = content[0:indexC]
        b = content[indexC:int(len(content))]
        content = a + doubleNewLine + snippet + doubleNewLine + b
        
        #write the new html file
        file = open(filepath, "w")
        file.writelines(content)
        file.close()
        
        print("Added new table to template " + templateName)
        
        
#Method to create a new tableEntry in a given column or page
def newTableEntry(templateName,title,subtitle,size,price):
    
    templateFilename = templateName + ".html"
    filepath = os.path.join(strpath,templateFilename)
    
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        file = open(filepath, "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(strpath, 'newTableEntry.html'), "r")
        snippet = file.readlines()
        file.close()
        
        #skipped the informationgathering on this one. Multiple placeholder in one line.
        
        
        #insert the paramaters into snippet
        snippet[1] = '                    <td>' + title + '<span class="small">' + subtitle + '</span></td>\n'
        snippet[2] = '                    <td><span class="small">' + size + '</span></td>\n'
        snippet[3] = '                    <td>' + price + '</td>\n'

        #get index of codeplacement and place snippet in content[indexC]
        indexC = -1
        for i in content:
            indexC = indexC + 1
            if cNewTable in i:
                break
               
        a = content[0:indexC]
        b = content[indexC:int(len(content))]
        content = a + doubleNewLine + snippet + doubleNewLine + b
        
        #write the new html file
        file = open(filepath, "w")
        file.writelines(content)
        file.close()
        
        print("Added new tableentry to template " + templateName)

#Method to copy the wanted template into folder "active page" to all the binaries and assets. Also tries to launch the site afterwards in firefox.
def showPage(templateName):
    
    templateFilename = templateName + ".html"
    filepath = os.path.join(strpath,templateFilename)
    activeFilepath = os.path.join(strpath, "activeSite", "getraenkekarte.html")
    
    if not os.path.isfile(filepath):
        print("Template does not exist!")
    else:
        file = open(filepath, "r")
        content = file.readlines()
        file.close()
        
        file = open(activeFilepath, "w")
        file.writelines(content)
        file.close()
        
        subprocess.call([firefoxPath,'-new-tab', activeFilepath])
        

#Main-Method, testing purposes only
if __name__ == "__main__":     
    removeTemplate(umlaut("peterenis"))
    newTemplate(umlaut("peterenis"))
    newPage(umlaut("peterenis"), umlaut("abc"), umlaut("abcd"))
    newColumn(umlaut("peterenis"))
    newTable(umlaut("peterenis"), umlaut("täbulator tabelle"))
    newTableEntry("peterenis", umlaut("bierÖ"), umlaut(3), "2,5", "3mark")
    newTableEntry("peterenis", umlaut("bier2"), umlaut(6), "45", "6mark")
    showPage("peterenis")
        