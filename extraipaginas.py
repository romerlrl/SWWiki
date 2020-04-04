#coding: UTF-8
import sys
caminho1="C:\\Users\\lucas\\Box Sync\\Star Wars\\SWW\\Scripts\\saida.csv"
caminho2="C:\\Users\\lucas\\Box Sync\\Star Wars\\SWW\\Scripts\\SWW2020-04.xml"
arquivo=open(caminho2, 'r', encoding='utf-8')
saida=open(caminho1, 'w', encoding='utf-8')
saida.write("titulo,tamanho,links,categorias,\n")
#Poupa a leitura dos primeiros 44 termos que são basicamente
#os atributos de <siteinfo>
notPreserve=[]
texto=False
for k in range(44):
    arquivo.readline()
print(arquivo.readline())
for k in arquivo:
    tag = k[:11]
    if tag=='    <title>':
        titulo=k[11:-9]
        titulo=titulo.replace(',', '_')
    elif tag=='      <text':        
        tamanho=k[40:]
        aux=tamanho.index('"')
        tamanho=tamanho[:aux]
        texto=True
        links=k.count('[[')
        categorias=0
    elif tag=='      <sha1':
        texto=False
        GoToCSV=(f"{titulo},{tamanho},{links},{categorias}\n")
        saida.write(GoToCSV)
        
    if texto:
        links+=k.count('[[')
        categorias+=k.count('[[Categoria:')
        categorias+=k.count('[[Category:')        
arquivo.close()
saida.close()
print('DONE')
