from math import *

def image (largeur,hauteur):
    matrice = [[1 for j in range(0,largeur)]for i in range(0,hauteur)]
    return matrice
   
def affiche (k):
    print (k)
    return

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
                     
                
def segment2(image,x1, y1, x2, y2):
    X=min(x1,x2)
    Y=min(y1,y2)

    if (x2-x1)==0:
        while (Y!=max(y1,y2)):
            image [Y][X]=0
            Y=Y+1
    else:
        if y2>y1:
            C=((y2-y1)/(x2-x1))
            b=y1-C*x1
            
            if C>0:
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)<=0:
                        image [Y][X]=0
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                    
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)>=0:
                        image [Y][X]=0
                        X=X-1
                    else:
                        X=X+1
                        Y=Y+1
        else:
            C=((y1-y2)/(x1-x2))
            b=y1-C*x1
            
            if C>0:
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)<=0:
                        image [Y][X]=0
                        X=X+1
                    else:
                        X=X-1
                        Y=Y+1
                    
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)>=0:
                        image [Y][X]=0
                        X=X-1
                    else:
                        X=X+1
                        Y=Y+1
        
            
            
    
def triangle(image,x1,y1,x2,y2,x3,y3,plein):
    if plein == False:
        segment2(image, x1, y1, x2, y2)
        segment2(image, x2, y2, x3, y3)
        segment2(image, x3, y3, x1, y1)
    else :
        segment2(image, x1, y1, x2, y2)
        segment2(image, x2, y2, x3, y3)
        segment2(image, x3, y3, x1, y1)
        i=0
        j=0
        
        while i != len(image)-1:
            while j != len(image[0])-1:
                if image[i][j] == 0:
                    while image[i][j]==0:
                        j=j+1
                    while image[i][j]==1 and j != len(image[0])-5:
                        image[i][j] = 0
                        j=j+1
                    while image[i][j]==0:
                        j=j+1
                j=j+1
            j=0
            i=i+1
    return

def triangle2(image,x1,y1,x2,y2,x3,y3):
    l1=y1+y2
    l2=y3+y2
    l3=y1+y3
    lmax= max(l1,l2,l3)
    p1=x1+x2
    p2=x3+x2
    p3=x1+x3
    pmax=max(p1,p2,p3)
    if 

def creation(text,nomFichier):
    p=open(nomFichier+".pgm", "w")
    p.write(text)
    p.close()


im=image(400,400)
segment2(im, 10,90, 20, 60)
segment2(im, 20,60, 10, 90)
segment2(im, 20,60, 30, 90)
segment2(im, 20,60, 40, 60)
#rectangle(im,20,200,20,20,False)
#rectangle(im,120,200,30,40,True)
#segment(im, 20,60, 50, 90)
#cercle(im,50,300,40,False)
#cercle(im,150,300,20,False)
#segment2(im, 0, 0, 399, 399,0)
triangle(im,20,30,200,30,340,340,False)
#affiche(convertion(im))
creation(convertion(im),'ot')



