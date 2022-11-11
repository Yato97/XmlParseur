from email.mime import application
from genericpath import isdir
from unittest.mock import patch
from colorama import Fore, Style
from os import listdir, walk
from os.path import isfile, join
import xml.etree.ElementTree as et

YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BRIGHT = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
CYAN = Fore.CYAN

list_repo = []
def init_menu():
    print(BRIGHT + MAGENTA + "------------- XMLPARSER -------------")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "1" +YELLOW + "]" +RESET + " - Ajouter header XML recursif")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "2" +YELLOW + "]" +RESET + " - Rechercher un fichier du workspace")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "3" +YELLOW + "]" +RESET + " - Parseur XML")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "4" +YELLOW + "]" +RESET + " - Analyseur XML")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "5" +YELLOW + "]" +RESET + " - Analyseur XML recursif")
    output = input("Outil sélectionné : ")
    return output

def router(output):
    # Output to the terminal is desired.
    if output == "1":
        print("\n"+BRIGHT + CYAN + "------------- XML TOOLS RECURSIF -------------"+ RESET)

        monRepertoire = input("Path du répertoire : ")
        for (repertoire, sousRepertoires, fichiers) in walk(monRepertoire):
            temp = repertoire
            for x in fichiers:
                file = temp+"\\"+x
                try :
                    if file.endswith(".application") or file.endswith(".package") or file.endswith(".model") or file.endswith(".form") or file.endswith(".xml") or file.endswith(".view"):
                        openfile = open(file, "r", encoding='utf-8-sig')
                        lignes = openfile.readline()
                        lignesAll = openfile.readlines()
                        openfile.close()
                        lignesAll[0] = '<?xml version="1.0" encoding="UTF-8" ?>'+"\n"+lignes
                        if(not(lignes.startswith('<?xml'))):
                            openfile = open(file, "w", encoding='utf-8-sig')
                            openfile.writelines(lignesAll)
                            openfile.close()
                            print(BRIGHT + YELLOW + "[" + GREEN + "+" + YELLOW + "]" + RESET + " - "+ CYAN + file)
                except UnicodeDecodeError as e:       
                    print(BRIGHT + YELLOW + "[" + RED + "-" + YELLOW + "]" + RESET + " - "+ CYAN + file + RESET + BRIGHT + RED + " : UNICODE ERROR : "+RESET,e.args[-1] + " : "+ e.args[0]) 

        ### ---------------------------------------------------------------------------------------------- ###
        
    if output == "2":
        print("\n"+BRIGHT + CYAN + "------------- FILE RESEARCHER -------------"+ RESET)
        monRepertoire = input("Path du workspace : ")
        fileResearsh = input("Nom du fichier : ")
        for (repertoire, sousRepertoires, fichiers) in walk(monRepertoire):
            temp = repertoire
            for x in fichiers:
                if fichiers == fileResearsh:
                    file = temp+"\\"+x
                    print(BRIGHT + YELLOW + "[" + GREEN + "+" + YELLOW + "]" + RESET + " - "+CYAN+file)
                    break
                
    if output == "3":
        print("\n"+BRIGHT + CYAN + "------------- XML PARSEUR -------------"+ RESET)
        monRepertoire = input("Path du fichier XML : ")
        my_tree = et.parse(monRepertoire)
        my_root = my_tree.getroot()

        for node in my_root:
            print("\n")
            print(BRIGHT + YELLOW + "[" + RED + "ROOT" + YELLOW + "]" + RESET, node.tag)
            for attr, res in node.attrib.items():
                print(BRIGHT + YELLOW + "[" + CYAN + "+" + YELLOW + "]" + RESET +" "+ CYAN + attr+ " : "+ BRIGHT +res)
            XMLparser(node, "|-")    
            
    if output == "4":
        print("\n"+BRIGHT + CYAN + "------------- XML ANALYSEUR -------------"+ RESET)
        monRepertoire = input("Path du fichier XML : ")
        XMLanalyseur(monRepertoire)  

    if output == "5":
        print("\n"+BRIGHT + CYAN + "------------- XML ANALYSEUR RECURSIF -------------"+ RESET)
        monRepertoire = input("Path repertoire a analyser : ")
        for (repertoire, sousRepertoires, fichiers) in walk(monRepertoire):
            temp = repertoire
            for x in fichiers:
                file = temp+"\\"+x
                if file.endswith(".application") or file.endswith(".package") or file.endswith(".model") or file.endswith(".form") or file.endswith(".xml") or file.endswith(".view"):
                    XMLanalyseurRec(file) 
        print("\n"+BRIGHT + GREEN + "END"+RESET) 

def XMLanalyseur(path):
    try:
        my_tree = et.parse(path)
        openfile = open(path, "r", encoding='utf-8-sig')
        lignes = openfile.readline()
        openfile.close()
        if(not(lignes.startswith('<?xml'))):
            print("\n"+BRIGHT + RED + "SYNTAX ERROR : "+RESET + "Missing header XML")
        else:
            print("\n"+BRIGHT + GREEN + "PASS"+RESET) 
    except et.ParseError as e:
        print("\n"+BRIGHT + RED + "SYNTAX ERROR : "+RESET, e.args) 
    except UnicodeDecodeError as e:       
        print(BRIGHT + YELLOW + "[" + RED + "-" + YELLOW + "]" + RESET + " - "+ CYAN + path + RESET + BRIGHT + RED + " : UNICODE ERROR : "+RESET,e.args[-1] + " : "+ e.args[0]) 
        
def XMLanalyseurRec(path):
    try:
        my_tree = et.parse(path)
        openfile = open(path, "r", encoding='utf-8-sig')
        lignes = openfile.readline()
        openfile.close()
        if(not(lignes.startswith('<?xml'))):
            print(BRIGHT + YELLOW + "[" + RED + "-" + YELLOW + "]" + RESET + " - "+ CYAN + path + RESET + BRIGHT + RED + " : SYNTAX ERROR : "+RESET + "Missing header XML")
    except et.ParseError as e:
        print(BRIGHT + YELLOW + "[" + RED + "-" + YELLOW + "]" + RESET + " - "+ CYAN + path + RESET + BRIGHT + RED + " : SYNTAX ERROR : "+RESET, e.args) 
    except UnicodeDecodeError as e:       
        print(BRIGHT + YELLOW + "[" + RED + "-" + YELLOW + "]" + RESET + " - "+ CYAN + path + RESET + BRIGHT + RED + " : UNICODE ERROR : "+RESET,e.args[-1] + " : "+ e.args[0]) 
        
        
def XMLparser(node, space):
    for child in node:
        print(space + BRIGHT + YELLOW + "[" + GREEN + "NODE" + YELLOW + "]" + RESET, child.tag)
        if len(child.attrib) != 0:
            for attr, res in child.attrib.items():
                print(RESET + space+CYAN+"|->" +BRIGHT + YELLOW + "[" + CYAN + "+" + YELLOW + "]" + RESET +" "+ CYAN + attr+ " : "+RESET + BRIGHT +res)

        if len(child) != 0:
            space = space + "|-"
            XMLparser(child, space)
            
     

if __name__ == "__main__":
    selector = init_menu()   
    router(selector)
