#!/usr/bin/env python
from math import *
from couleur import *
from sys import argv
import random

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
        T[2]=image(200,200,couleur["Blanc"])
        rectangle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]), T[7], couleur[T[8]])
        creation(convertion(T[2]), NomIm)

    elif T[1] == "--cercle" :
        NomIm = T[2]
        T[2]=image(200,200,couleur["Blanc"])
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), T[6],couleur[T[7]])
        creation(convertion(T[2]), NomIm)

    elif T[1] == "--segment" :
        NomIm = T[2]
        T[2]=image(200,200,couleur["Blanc"])
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]),T[7],T[8])
        creation(convertion(T[2]),NomIm)

    elif T[1] == "--triangle" :
        NomIm = T[2]        
        T[2]=image(200,200,couleur["Blanc"])
        cercle (T[2], int(T[3]), int(T[4]), int(T[5]), int(T[6]), int(T[7]), int(T[8]), T[9],T[10])
        creation(convertion(T[2]),NomIm)

    elif T[1] == "--point" :
        NomIm = T[2]        
        T[2]=image(200,200,couleur["Blanc"])
        point (T[2], int(T[3]), int(T[4]), couleur[T[5]])
        creation(convertion(T[2]),NomIm)
        
    else : print ("error")
    
def image (largeur,hauteur,couleur):
    matrice = [[couleur for j in range(0,largeur)]for i in range(0,hauteur)]
    return matrice

def convertion (image):             
    k='P3\n'
    k=k+str(len(image))+' '+str(len(image[0]))+'\n'
    k=k+str(255)+'\n'
    for i in range (0,len(image)):
        for j in range (0,len(image[0])):
            if j!=0 :
                k=k+' '+str((image[i][j]))
            else:
                k=k+str((image[i][j]))
        k=k+'\n'        
    return k

def point (image,x,y,couleur):
    image[y][x]=couleur
    
def rectangle (image,x,y,hauteur,largeur,plein,couleur):
     for i in range (y-1, y+hauteur-1):
         for j in range (x-1,x+largeur-1):
             if plein :
                 image[i][j]=couleur
             elif j==x-1 or j==x+largeur-2 or i==y-1 or i==y+hauteur-2:
                 image[i][j]=couleur
                     
def cercle (image,x,y,rayon,plein,couleur):
     for i in range (y-rayon,y+rayon+1):
         for j in range (x-rayon,x+rayon+1):
             if plein ==False :
                 if (j-x)**2 + (i-y)**2 < rayon**2+rayon and (j-x)**2 + (i-y)**2> rayon**2-rayon:
                     image[i][j]=couleur
             else:
                 if (j-x)**2 + (i-y)**2 <= rayon**2:
                     image[i][j]=couleur
                
def segment(image,x1, y1, x2, y2,couleur,CreeTab=False):
    Y=min(y1,y2)
    if Y==y1:
        X=x1
    else:
        X=x2
    T=[]
    if CreeTab:
        None
        #T=T+[(X,Y)]
    else:
        image [Y][X]=couleur
                
    if (x2-x1)==0:
        while (Y<max(y1,y2)):
            if CreeTab:
                T=T+[(X,Y)]
            else:
                image [Y][X]=couleur
            Y=Y+1
    else:
        if y2>y1:
            C=((y2-y1)/(x2-x1))
            b=y1-C*x1
            if C>0:
                while (Y<=max(y1,y2)):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)<=0:
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
                if CreeTab:
                    T=T+[(X,Y)]
            else:
                X=max(x1,x2)
                while (Y<=max(y1,y2)):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)>=0:
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X-1
                    else:
                        X=X+1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
        else:
            C=((y1-y2)/(x1-x2))
            b=y1-C*x1
            
            if C>0:
                while (Y<=max(y1,y2)):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)<=0:
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
            else:
                X=max(x1,x2)
                while (Y<=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)>=0:
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X-1
                    else:
                        X=X+1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
    if CreeTab:
        return T
    else:
        return None
    
def reduit (x1,x2,x3,y1,y2,y3,couleur):
    if y1==min(y1,y2):
        if x1>x3:
            print ('1')
            TG=segment(image,x1,y1,x2,y2,True,couleur)
            TD=segment(image,x1,y1,x3,y3,True,couleur)+segment(image,x3,y3,x2,y2,True,couleur)
        else:
            print ('2')
            TD=segment(image,x1,y1,x2,y2,True,couleur)
            TG=segment(image,x1,y1,x3,y3,True,couleur)+segment(image,x3,y3,x2,y2,True,couleur)
    else :
        if x2>x3:
            print ('3')
            TG=segment(image,x2,y2,x1,y1,True,couleur)
            TD=segment(image,x2,y2,x3,y3,True,couleur)+segment(image,x3,y3,x1,y1,True,couleur)
        else:
            print ('4')
            TD=segment(image,x2,y2,x1,y1,True,couleur)
            TG=segment(image,x2,y2,x3,y3,True,couleur)+segment(image,x3,y3,x1,y1,True,couleur)
    return (TD,TG)
    
def triangle(image,xa,ya,xb,yb,xc,yc,couleur,plein):
    l1=max(ya,yb)-min(ya,yb)
    l2=max(yc,yb)-min(yc,yb)
    l3=max(ya,yc)-min(ya,yc)
    j=0
    lmax= max(l1,l2,l3)
    if plein == False :
        segment(image, xa, ya, xb, yb,couleur)
        segment(image, xb, yb, xc, yc,couleur)
        segment(image, xc, yc, xa, ya,couleur)
    else:
        if l1==lmax:
            TD,TG=reduit(xa,xb,xc,ya,yb,yc,couleur)
        elif l2==lmax:
            TD,TG=reduit(xb,xc,xa,yb,yc,ya,couleur)
        else :
            TD,TG=reduit(xc,xa,xb,yc,ya,yb,couleur)
        print (len(TD),len(TG))
        
        for o in range(0,len(TD)-1):
            for m in range(TD[o][0],TG[o][0]):
                image[TD[o][1]][m]=couleur
    
def creation(text,nomFichier):
    p=open(nomFichier+".ppm", "w")
    p.write(text)
    p.close()

if __name__ == "__main__" :
    appelle_fonction()
    




