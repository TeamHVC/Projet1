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
        im=image(200,200,couleur["Blanc"])
        if T[6]=="True":
            rectangle (im, int(T[2]), int(T[3]), int(T[4]), int(T[5]), True, couleur[T[7]])
        else :
            rectangle (im, int(T[2]), int(T[3]), int(T[4]), int(T[5]), False, couleur[T[7]])
        creation(convertion(im),"flute")
        
    elif T[1] == "--cercle" :
        im=image(200,200,couleur["Blanc"])
        if T[6]=="True":
            cercle (im, int(T[3]), int(T[4]), int(T[5]), True,couleur[T[7]])
        else:
            cercle (im, int(T[3]), int(T[4]), int(T[5]), False,couleur[T[7]])
        creation(convertion(im),T[2])

    elif T[1] == "--segment" :
        im=image(200,200,couleur["Blanc"])
        segment(im, int(T[3]), int(T[4]), int(T[5]), int(T[6]),couleur[T[7]])
        creation(convertion(im),T[2])

    elif T[1] == "--triangle" :
        im=image(200,200,couleur["Blanc"])
        if T[10]=="True" :          
            triangle(im, int(T[3]), int(T[4]), int(T[5]), int(T[6]), int(T[7]), int(T[8]), couleur[T[9]],True)
        else :
            triangle (im, int(T[3]), int(T[4]), int(T[5]), int(T[6]), int(T[7]), int(T[8]), couleur[T[9]],False)
        creation(convertion(im),T[2])
        
    elif T[1] == "--point" :
        im=image(200,200,couleur["Blanc"])      
        point (im, int(T[3]), int(T[4]), couleur[T[5]])
        creation(convertion(im),T[2])
        
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
                
def segment(image,x1, y1, x2, y2,couleur,CreeTab=False,cube=False):
    
    Y=min(y1,y2)
    if Y==y1:
        X=x1
    else:
        X=x2
    T=[]
    if x1==x2:
       
        while (Y<=max(y1,y2)):
            if CreeTab:
                T=T+[(X,Y)]
            else:
                image [Y][X]=couleur
            Y=Y+1
    elif y1==y2:
        
        if CreeTab:
                T=T+[(X,Y)]
        for i in range(min(x1,x2),max(x1,x2)):
            if CreeTab==False:
                image [Y][i]=couleur
    else:
        
        if y2>y1:
            print(str(y2)+" "+str(y1)+" "+str(x2)+" "+str(x1))
            C=((y2-y1)/(x2-x1))
            
            print("C = "+(str((y2-y1)//(x2-x1))))
            b=y1-C*x1
            print("b = "+(str(y1-C*x1)))
            if C>0:
                while (Y<=max(y1,y2)):
        
                    print((y2-y1)*X-Y*(x2-x1)+b*(x2-x1))
                    if ((y2-y1)*X-Y*(x2-x1)+b*(x2-x1)<=0 or (X==max(x1,x2) and Y==min(y1,y2))):

                        
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X+1
                    else:
                        
                        X=X-1
                        if CreeTab and not cube:
                            T=T+[(X,Y)]
                        cube=False
                        Y=Y+1
            else:
                X=max(x1,x2)
                
                while (Y<=max(y1,y2)):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)>=0 or (X==max(x1,x2) and Y==min(y1,y2)):
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X-1
                    else:
                        X=X+1
                        if CreeTab and not cube:
                            T=T+[(X,Y)]
                        cube=False
                        Y=Y+1
                        
        else:
            C=((y1-y2)/(x1-x2))
            
            b=y1-C*x1
            
            if C>0:
                while (Y<=max(y1,y2)):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)<=0 or (X==max(x1,x2) and Y==min(y1,y2)):
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X+1
                    else:
                        X=X-1
                        if CreeTab and not cube:
                            T=T+[(X,Y)]
                        cube=False
                        Y=Y+1
                        
            else:
                
                X=max(x1,x2)
                while (Y<=max(y1,y2)):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)>=0 or (X==max(x1,x2) and Y==min(y1,y2)):
                        if CreeTab==False:
                            image [Y][X]=couleur
                        X=X-1
                    else:
                        X=X+1
                        if CreeTab and not cube:
                            T=T+[(X,Y)]
                            cube=True
                        Y=Y+1
    
    if CreeTab:
        return T
    else:
        return None
    
def reduit (x1,x2,x3,y1,y2,y3,couleur):
    if x1==x2:
        if(y1==min(y1,y2)):
            if x3>x1:
               
                TD=segment(image,x1,y1,x3,y3,couleur,True)+segment(image,x3,y3,x2,y2,couleur,True,True)
                TG=segment(image,x1,y1,x2,y2,couleur,True)
            else:
                
                TG=segment(image,x1,y1,x3,y3,couleur,True)+segment(image,x3,y3,x2,y2,couleur,True,True)
                TD=segment(image,x1,y1,x2,y2,couleur,True)
        else:
            if x3>x1:
                
                TD=segment(image,x2,y2,x3,y3,couleur,True)+segment(image,x3,y3,x1,y1,couleur,True,True)
                TG=segment(image,x2,y2,x1,y1,couleur,True)
            else:
                
                TG=segment(image,x2,y2,x3,y3,couleur,True)+segment(image,x3,y3,x1,y1,couleur,True,True)
                TD=segment(image,x2,y2,x1,y1,couleur,True)
    else:  
        C=((y2-y1)/(x2-x1))
        b=(y1)-(C*x1)
        
        if y1==min(y1,y2):
            if ((y1-y2)*x3-y3*(x1-x2)+b*(x1-x2)<=0 and C>=0) or ((y1-y2)*x3-y3*(x1-x2)+b*(x1-x2)<=0 and C<=0):
                TD=segment(image,x1,y1,x3,y3,couleur,True)+segment(image,x3,y3,x2,y2,couleur,True,True)
                TG=segment(image,x1,y1,x2,y2,couleur,True)
            elif ((y1-y2)*x3-y3*(x1-x2)+b*(x1-x2)>=0 and C>=0) or ((y1-y2)*x3-y3*(x1-x2)+b*(x1-x2)>=0 and C<=0):
                TG=segment(image,x1,y1,x3,y3,couleur,True)+segment(image,x3,y3,x2,y2,couleur,True,True)
                TD=segment(image,x1,y1,x2,y2,couleur,True)
        else:
            if ((y2-y1)*x3-y3*(x2-x1)+b*(x2-x1)<=0 and C>=0) or ((y2-y1)*x3-y3*(x2-x1)+b*(x2-x1)<=0 and C<=0):
                TD=segment(image,x2,y2,x3,y3,couleur,True)+segment(image,x3,y3,x1,y1,couleur,True,True)
                TG=segment(image,x2,y2,x1,y1,couleur,True)
            elif ((y2-y1)*x3-y3*(x2-x1)+b*(x2-x1)>=0 and C>=0) or ((y2-y1)*x3-y3*(x2-x1)+b*(x2-x1)>=0 and C<=0):
                TG=segment(image,x2,y2,x3,y3,couleur,True)+segment(image,x3,y3,x1,y1,couleur,True,True)
                TD=segment(image,x2,y2,x1,y1,couleur,True)
            
    return (TD,TG)
    
def triangle(image,xa,ya,xb,yb,xc,yc,couleur,plein):
    l1=max(ya,yb)-min(ya,yb)
    l2=max(yc,yb)-min(yc,yb)
    l3=max(ya,yc)-min(ya,yc)
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
        for o in range(0,len(TD)-1):
            for m in range(TG[o][0],TD[o][0]):
                image[TG[o][1]][m]=couleur
    
def creation(text,nomFichier):
    p=open(nomFichier+".ppm", "w")
    p.write(text)
    p.close()

if __name__ == "__main__" :
    appelle_fonction()
    



