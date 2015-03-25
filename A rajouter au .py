#!/usr/bin/env python
from sys import argv


def affiche_args() :
    T_Arg = []
    print ("Les arguements sont : ")
    for arg in argv :
        print (arg)
        T_Arg = T_Arg + [arg]

    return T_Arg

def appelle_fonction ():
    T = affiche_args()
    
    if T[1] == "--rectangle" :
        NomIm = T[2]
        T[2]=image(200,200)
        rectangle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]), T[7])
        creation(convertion(T[2]), NomIm)

    elif T[1] == "--cercle" :
        NomIm = T[2]
        T[2]=image(200,200)
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), T[6])
        creation(convertion(T[2]), NomIm)

    elif T[1] == "--segment" :
        NomIm = T[2]
        T[2]=image(200,200)
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]))
        creation(convertion(T[2]),NomIm)

    elif T[1] == "--triangle" :
        NomIm = T[2]        
        T[2]=image(200,200)
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]), int(T[7]), int(T[8]), T[9])
        creation(convertion(T[2]),NomIm)
        
    else : print ("error")

## AJOUTER A LA FIN :
if __name__ == "__main__" :
    appelle_fonction()
    
## Enlever à la fin : Définition de l'image + Appel de la fonction Création

