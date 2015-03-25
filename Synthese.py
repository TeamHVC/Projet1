from math import *

import random
def image (largeur,hauteur):
    matrice = [[1 for j in range(0,largeur)]for i in range(0,hauteur)]
    return matrice

def convertion (image):
    max=0
    for i in range (0,len(image)):
        for j in range (0,len(image[0])):
            if max < image[i][j] :
                max = image[i][j]
                
    k='P2\n'
    k=k+str(len(image))+' '+str(len(image[0]))+'\n'
    k=k+str(max)+'\n'
    for i in range (0,len(image)):
        for j in range (0,len(image[0])):
            if j!=0 :
                k=k+' '+str((image[i][j]))
            else:
                k=k+str((image[i][j]))
        k=k+'\n'        
    return k

def rectangle (image,x,y,hauteur,largeur,plein):
     for i in range (y-1, y+hauteur-1):
         for j in range (x-1,x+largeur-1):
             if plein :
                 image[i][j]=0
             elif j==x-1 or j==x+largeur-2 or i==y-1 or i==y+hauteur-2:
                 image[i][j]=0

def cercle (image,x,y,rayon,plein):
     for i in range (y-rayon,y+rayon+1):
         for j in range (x-rayon,x+rayon+1):
             if plein ==False :
                 if (j-x)**2 + (i-y)**2 < rayon**2+rayon and (j-x)**2 + (i-y)**2> rayon**2-rayon:
                     image[i][j]=0
             else:
                 if (j-x)**2 + (i-y)**2 <= rayon**2:
                     image[i][j]=0   
                
def segment(image,x1, y1, x2, y2,CreeTab=False):
    X=min(x1,x2)
    Y=min(y1,y2)
    T=[]
    if CreeTab:
        T=T+[(X,Y)]
    else:
        image [Y][X]=0
                
    if (x2-x1)==0:
        while (Y!=max(y1,y2)):
            if CreeTab:
                T=T+[(X,Y)]
            else:
                image [Y][X]=0
            Y=Y+1
    else:
        if y2>y1:
            C=((y2-y1)/(x2-x1))
            b=y1-C*x1
            
            if C>0:
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)<=0:
                        if CreeTab==False:
                            image [Y][X]=0
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)>=0:
                        if CreeTab==False:
                            image [Y][X]=0
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
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)<=0:
                        if CreeTab==False:
                            image [Y][X]=0
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                        if CreeTab:
                            T=T+[(X,Y)]
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)>=0:
                        if CreeTab==False:
                            image [Y][X]=0
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
    
def reduit (x1,x2,x3,y1,y2,y3):
    if y1==min(y1,y2):
        if x1>x3:
            print ('1')
            TG=segment(image,x1,y1,x2,y2,True)
            TD=segment(image,x1,y1,x3,y3,True)+segment(image,x3,y3,x2,y2,True)
        else:
            print ('2')
            TD=segment(image,x1,y1,x2,y2,True)
            TG=segment(image,x1,y1,x3,y3,True)+segment(image,x3,y3,x2,y2,True)
    else :
        if x2>x3:
            print ('3')
            TG=segment(image,x2,y2,x1,y1,True)
            TD=segment(image,x2,y2,x3,y3,True)+segment(image,x3,y3,x1,y1,True)
        else:
            print ('4')
            TD=segment(image,x2,y2,x1,y1,True)
            TG=segment(image,x2,y2,x3,y3,True)+segment(image,x3,y3,x1,y1,True)
    return (TD,TG)
    
def triangle(image,xa,ya,xb,yb,xc,yc,plein):
    l1=max(ya,yb)-min(ya,yb)
    l2=max(yc,yb)-min(yc,yb)
    l3=max(ya,yc)-min(ya,yc)
    j=0
    lmax= max(l1,l2,l3)
    if plein == False :
        segment(image, xa, ya, xb, yb)
        segment(image, xb, yb, xc, yc)
        segment(image, xc, yc, xa, ya)
    else:
        if l1==lmax:
            TD,TG=reduit(xa,xb,xc,ya,yb,yc)
        elif l2==lmax:
            TD,TG=reduit(xb,xc,xa,yb,yc,ya)
        else :
            TD,TG=reduit(xc,xa,xb,yc,ya,yb)
        print (len(TD),len(TG))
        
        for o in range(0,len(TD)-1):
            for m in range(TD[o][0],TG[o][0]):
                image[TD[o][1]][m]=0

def creation(text,nomFichier):
    p=open(nomFichier+".pgm", "w")
    p.write(text)
    p.close()


im=image(400,400)
#rectangle(im,20,200,20,20,False)
#rectangle(im,120,200,30,40,True)
#segment2(im, 20,60, 50, 90)
#cercle(im,50,300,40,False)
#cercle(im,150,300,20,False)
#segment2(im, 0, 0, 399, 399,0)
#affiche(convertion(im))
#triangle2(im,34,150,56,200,150,24)
#triangle(im,34,150,56,200,150,24,False)
for i in range (0,100):
    x1=random.randint(0,399)
    x2=random.randint(0,399)
    x3=random.randint(0,399)
    y1=random.randint(0,399)
    y2=random.randint(0,399)
    y3=random.randint(0,399)
    print(str(x1)+' ,'+str(y1)+' ,'+str(x2)+' ,'+str(y2)+' ,'+str(x3)+' ,'+str(y3))
    triangle(im,x1,y1,x2,y2,x3,y3,True)
#triangle(im,40 ,329 ,156 ,163 ,163 ,210,False)
#triangle2(im,x1,y1,x2,y2,x3,y3,True)
#segment2(im, 210, 349, 286 ,381,False)
#segment2(im, 286 ,381, 355, 285,False)
#segment2(im, 355, 285, 210, 349,False)
#triangle2(im,204 ,69, 327 ,120 ,41 ,373,True)

creation(convertion(im),'o')





