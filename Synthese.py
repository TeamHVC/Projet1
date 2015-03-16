from math import *
import random
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
                        
def segmentTab(x1, y1, x2, y2):
    X=min(x1,x2)
    Y=min(y1,y2)
    T=[]
    i=0
    if (x2-x1)==0:
        while (Y!=max(y1,y2)):
            T=T+[(X,Y)]
            Y=Y+1
    else:
        if y2>y1:
            C=((y2-y1)/(x2-x1))
            b=y1-C*x1
            
            if C>0:
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)<=0:
                        X=X+1
                    else:
                        
                        X=X-1
                        T=T+[(X,Y)]
                        Y=Y+1
                    
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y2-y1)*X-Y*(x2-x1)+b*(x2-x1)>=0:
                       
                        X=X-1
                    else:
                        
                        X=X+1
                        T=T+[(X,Y)]
                        Y=Y+1
        else:
            C=((y1-y2)/(x1-x2))
            b=y1-C*x1
            
            if C>0:
                while (X!=max(x1,x2)+1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)<=0:
                        
                        X=X+1
                    else:
                        
                        X=X-1
                        T=T+[(X,Y)]
                        Y=Y+1
                    
            else:
                X=max(x1,x2)
                while (X!=min(x1,x2)-1 and Y!=max(y1,y2)+1):
                    if (y1-y2)*X-Y*(x1-x2)+b*(x1-x2)>=0:
                        X=X-1
                    else:
                        X=X+1
                        T=T+[(X,Y)]
                        Y=Y+1
    return T
            
            
    
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

def triangle2(image,xa,ya,xb,yb,xc,yc):
    #l1=ya+yb
    #l2=yc+yb
    #l3=ya+yc
    l1=max(ya,yb)-min(ya,yb)
    l2=max(yc,yb)-min(yc,yb)
    l3=max(ya,yc)-min(ya,yc)
    j=0
    lmax= max(l1,l2,l3)
    
    if l1==lmax:
        print ('l1')
        x1=xa
        x2=xb
        x3=xc
        y1=ya
        y2=yb
        y3=yc
        if y1==min(y1,y2):
            if x1>x3:
                print ('1')
                TG=segmentTab(x1,y1,x2,y2)
                TD=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
            else:
                print ('2')
                TD=segmentTab(x1,y1,x2,y2)
                TG=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
        else :
            if x2>x3:
                print ('3')
                TG=segmentTab(x2,y2,x1,y1)
                TD=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
            else:
                print ('4')
                TD=segmentTab(x2,y2,x1,y1)
                TG=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
    elif l2==lmax:
        print ('l2')
        x1=xb
        x2=xc
        x3=xa
        y1=yb
        y2=yc
        y3=ya
        if y1==min(y1,y2):
            if x1>x3:
                print ('1')
                TG=segmentTab(x1,y1,x2,y2)
                TD=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
            else:
                print ('2')
                TD=segmentTab(x1,y1,x2,y2)
                TG=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
        else :
            if x2>x3:
                print ('3')
                TG=segmentTab(x2,y2,x1,y1)
                TD=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
            else:
                print ('4')
                TD=segmentTab(x2,y2,x1,y1)
                TG=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
            
    else :
        print ('l3')
        x1=xc
        x2=xa
        x3=xb
        y1=yc
        y2=ya
        y3=yb
        if y1==min(y1,y2):
            if x1>x3:
                print ('1')
                TG=segmentTab(x1,y1,x2,y2)
                TD=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
            else:
                print ('2')
                TD=segmentTab(x1,y1,x2,y2)
                TG=segmentTab(x1,y1,x3,y3)+segmentTab(x3,y3,x2,y2)
        else :
            if x2>x3:
                print ('3')
                TG=segmentTab(x2,y2,x1,y1)
                TD=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
            else:
                print ('4')
                TD=segmentTab(x2,y2,x1,y1)
                TG=segmentTab(x2,y2,x3,y3)+segmentTab(x3,y3,x1,y1)
    print (len(TD),len(TG))
    affichle(TD,TG)
    for o in range(0,len(TD)-1):
        for m in range(TD[o][0],TG[o][0]):
            image[TD[o][1]][m]=0

def affichle(t,t2):
    for i in range(len (t)):
        print (str(t[i])+'   '+str(t2[i])+'\n')
def creation(text,nomFichier):
    p=open(nomFichier+".pgm", "w")
    p.write(text)
    p.close()


im=image(400,400)
#rectangle(im,20,200,20,20,False)
#rectangle(im,120,200,30,40,True)
#segment(im, 20,60, 50, 90)
#cercle(im,50,300,40,False)
#cercle(im,150,300,20,False)
#segment2(im, 0, 0, 399, 399,0)
#affiche(convertion(im))
#triangle2(im,34,150,56,200,150,24)
#triangle(im,34,150,56,200,150,24,False)
x1=random.randint(0,399)
x2=random.randint(0,399)
x3=random.randint(0,399)
y1=random.randint(0,399)
y2=random.randint(0,399)
y3=random.randint(0,399)
print(str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)+' '+str(x3)+' '+str(y3))
triangle(im,x1,y1,x2,y2,x2,y3,False)
triangle2(im,x1,y1,x2,y2,x2,y3)
#triangle2(im,286 ,241 ,59 ,237 ,359, 147)
#triangle(im,286 ,241 ,59 ,237 ,359 ,147,False)
creation(convertion(im),'ot')




