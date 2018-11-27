'''
Created on 27.11.2018

@author: Anton
'''

import os

#!!! gegenchecken ob auch auf Linux funktionell!!!
strpath = os.path.join('D:\\', 'Desktop', 'pyfolder')

#Variablenzuweisung fuer die Suchebegriffe in den Template files
cTemplate = "<!--code_template17040512773411457715-->"
cNewPage = "<!--code_newPage05565400559591493791-->"
cNewColumn = "<!--code_newColumn99082008157953769982-->"
cNewTable = "<!--code_newTable88824758446917230372-->"
gifNewPage = "<!--gif-name42400233872280850289-->"
nameNewTable = "<!--table-name54845187244651894351-->"
titleNewEntry = "<!--entry-title69268835613672992291-->"
subtitleNewEntry = "<!--subtitle20695851250842941751-->"
sizeNewEntry = "<!--entry-size32101880553337566628-->"
priceNewEntry = "<!--entry-price45117288500038563995-->"

def newTemplate(name):
    
    filename = name + ".html"
    
    if os.path.isfile(os.path.join(strpath, filename)):
        print("File/Folder already exists!")
    else:
        file = open(os.path.join(strpath, 'template.html'), "r")
        content = file.readlines()
        file.close()
        
        file = open(os.path.join(strpath, filename), "w")
        file.writelines(content)
        file.close()
    
    

# concatenated the standardpath mit dem filename
filepath1 = os.path.join(strpath, 'test1.txt')
file = open(filepath1,"r")
print(file.readlines())
file.close()
newTemplate("peterenis")
