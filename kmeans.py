from random import * 
from math import sqrt
import matplotlib.pyplot as plt
def affichage(tab):
	for i in range(len(tab[0])):
		for j in range(len(tab[0][i])):
			print(" | ",tab[0][i][j],end="")
		print(" |     ",tab[1][i])

def affichagePoint(tab):
    if len(tab)!=0:
        for i in range(len(tab)):
            print(" | ",tab[i],end="")
        print(" |")
            
def compare2P(p1,p2): # si 2 points sont différents entre eux
    for i in range(len(p1)):
        for j in range(len(p1[i])):

            if p1[i][j] != p2[i][j]:
                return True
    return False
def copier(p1,p2):
    for i in range(len(p1)):
        for j in range(len(p1[i])):
            p1[i][j]=p2[i][j]
    return p1


def kmeans(tab, k):

    affichage(tab)

    nEff = len(tab[0])//k
    points=dict()
    sauvegarde=dict()

    for i in range(k):
        points[i]=dict()
        sauvegarde[i]=dict()
        for j in range(len(tab[0][0])):
            sauvegarde[i][j]=999999999
            points[i][j]=88888

        print("--------------------\n")
        affichagePoint(points[i])

    print("--------------------\n")

    diff=dict()

    while compare2P(points,sauvegarde):    #le boucle continue tant que les cluesteurs bouge

        sauvegarde=copier(sauvegarde,points)
        print("---------------------------------------------------------")
        affichage(tab)
        
        for l in range(k):# initilisation des 3 centroïdes a l aide des points dans chaques groupes
            
            for j in range(len(tab[0][1])):
                sommes=0
                div=0
                for i in range(len(tab[0])):
                    if tab[1][i]==l:
                        sommes+= tab[0][i][j]
                        div+=1
                if div!=0:
                    points[l][j]=sommes/div
        print("---------------------------------------------------------")            
        affichagePoint(points[0])
        affichagePoint(points[1])
        affichagePoint(points[2])
        affichagePoint(sauvegarde[0])
        affichagePoint(sauvegarde[1])
        affichagePoint(sauvegarde[2])
        print("---------------------------------------------------------")
        for i in range(len(tab[0])):    #parcourir tous les points 

            for j in range(k):#
                diff[j]=0
                for y in range(len(points[0])):
                    diff[j]+=(points[j][y]-tab[0][i][y])**2
                diff[j]=sqrt(diff[j])

            print(diff)
            petit = diff[0]
            sortie = 0
            for j in range(1,k):
                if petit > diff[j]:
                    petit = diff[j]
                    sortie = j
            tab[1][i]=sortie


    list=dict()
    for i in range(k):
    	list[i]=dict()
    	list[i][0]=[]
    	list[i][1]=[]


    for i in range (len(tab[1])):
        if(tab[1][i]==0):
            list[0][0].append(tab[0][i][1])
            list[0][1].append(tab[0][i][2])
            
        elif(tab[1][i]==1):
            list[1][0].append(tab[0][i][1])
            list[1][1].append(tab[0][i][2])

        elif(tab[1][i]==2):
            list[2][0].append(tab[0][i][1])
            list[2][1].append(tab[0][i][2])
            

    plt.plot(list[0][0], list[0][1], "r^")
    plt.plot(list[1][0], list[1][1], "bs")
    plt.plot(list[2][0], list[2][1], "g^")
    affichage(tab)
    plt.show()
    

def tp(nbPoint,dimension,nbCentroide):

	tab=dict()

	tab[0]=dict()
	for i in range(nbPoint):
		tab[0][i]=dict()
		for j in range(dimension):
			tab[0][i][j]=randint(1, 150)
	tab[1]=[]
	for i in range(nbPoint):
			
		tab[1].append(i%nbCentroide)
		
	kmeans(tab,nbCentroide)

def tp_data(fichier,nbCentroide):
    with open(fichier, 'r') as mon_fichier:

        list=mon_fichier.read().split("\n")

        mon_fichier.close()

    for i in range(len(list)):
        list[i]=list[i].split(',')
    
    tab=dict()

    tab[0]=list
    tab[1]=[]
    print(list)
    for i in range(len(list)):
        tab[1].append((i)%nbCentroide)
        # if i<=50:
        #     tab[1].append(0)
            
        # elif(i>50 and i<=100):
        #     tab[1].append(1)
        # else:
        #     tab[1].append(2)
        for j in range(len(tab[0][0])):
            
            tab[0][i][j]=float(tab[0][i][j])
            #print(tab[0][i][j])
    kmeans(tab,nbCentroide)

#tp(60,2,3)
tp_data("data.txt",5)