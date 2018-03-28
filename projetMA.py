from random import * 
from reseau import *
def Affiche(Tab) :
	
	i=0
	n=len(Tab[0])
	while i<n:
		j=0
		print("| ",end='')
		while j<n:
			if(Tab[0][i][j]<0.00001 and Tab[0][i][j] > -0.00001):
				print("0",end='  ')
			else:
				print(Tab[0][i][j],end='  ')
			j=j+1
		print("| ",Tab[1][i]," |\n")
		i=i+1


def echange(Tab,l1,l2):#O(n)
	for i in range (0,len(Tab[0])):
		Tab[0][l1][i],Tab[0][l2][i]=Tab[0][l2][i],Tab[0][l1][i]
		
	Tab[1][l1],Tab[1][l2]=Tab[1][l2],Tab[1][l1]
	return Tab

def calculLigne(Tab,pivot,cible,colonne):#O(n)

	coef=Tab[0][cible][colonne]/Tab[0][pivot][colonne]
	for i in range (0,len(Tab[0])):
		Tab[0][cible][i]=Tab[0][cible][i] - coef * Tab[0][pivot][i]
		
	Tab[1][cible]=Tab[1][cible] - coef * Tab[1][pivot]
	return Tab
	
def organiser(Tab,pivot):#O(n^2)
	
	k=0
	while pivot+k < len(Tab[0]):
		if Tab[0][pivot][pivot+k]==0:
			i,n=pivot+1,len(Tab[0])
			while i<n :
				if Tab[0][i][pivot+k]!=0 :
					Tab=echange(Tab,pivot,i)
					return Tab
				i=i+1
		else:
			return Tab
		k+=1
	return Tab

def SiSolution(Tab):#O(n^2)
	n=len(Tab[0])
	
	for i in range (0,n):
		retour=False
		for j in range(0,n):
			if(Tab[0][i][j]!=0):
				retour=True
		if(retour==False and Tab[1][i]!=0):
			return False
	return True

def pivotGauss(Tab):#O(n^3)
	n=len(Tab[0])
	colonne = 0
	for i in range(0,n):#O(n^3)
		# print(i,colonne,"1")
		# Affiche(Tab)
		# print("")
		
		if Tab[0][i][colonne]==0:
			Tab = organiser(Tab,i)#O(n^2)
		
		# print(i,colonne,"2")
		# Affiche(Tab)

		if Tab[0][i][colonne]==0:
			colonne+=1
		if colonne==n:
			break
		for j in range(i+1,n): #boucle pour calculer les lignes en dessous 
			
			if(Tab[0][j][colonne]!=0):
				Tab=calculLigne(Tab,i,j,colonne)#O(n)

		colonne+=1
		if colonne==n:
			break
	if(SiSolution(Tab)):#O(n^2)
		return Tab
	else:
		return False

def remonterGaus(tab):#O(n^2)
	n=len(tab[0])
	i=n-1
	colonne=n-1
	while i>=0 and colonne>=0:
		
		if tab[0][i][colonne] > -0.000000000001 and tab[0][i][colonne] < 0.000000000001:
			tab[0][i][colonne]=0
		if tab[0][i][colonne]!=0: #division 
			coef=tab[0][i][colonne]
			
			for alex in range(i,n):
				tab[0][i][alex]/=coef
			tab[1][i]/=coef				
			ligne=1
			while ligne <= i:#soustration
				
				coef=-1*tab[0][i-ligne][colonne]
	
				alex=n-1
				while alex>i-1:
					# print("cible",tab[0][i-ligne][alex],"pivot",tab[0][i][alex],"avant")
					# Affiche(tab)
					
					tab[0][i-ligne][alex]+=tab[0][i][alex]*coef
					
					# print("cible",tab[0][i-ligne][alex],"pivot",tab[0][i][alex],"apres")
					
					alex-=1
				tab[1][i-ligne]+=tab[1][i]*coef

				ligne+=1

		i-=1
		colonne-=1

	return tab


def solution(tab):
	n=len(tab[1])
	i=0
	col=0
	libre=dict()
	while i<n and col<n:
		if(tab[0][i][col]==0):
			libre[len(libre)]=col
			col+=1
		i+=1
		col+=1

	for i in range(len(libre)):
		tab[1][libre[i]]="X"+ str(libre[i]+1)

	i=n-1
	col=n-1
	while i>=0 and col >= 0:
		if isinstance(tab[1][i],float) or isinstance(tab[1][i],int):
			ntm =tab[1][i]
			tab[1][i]=str(tab[1][i])
			alex=col+1
			while alex<=n-1:
				if(tab[0][i][alex]!=0):
					if(tab[0][i][alex]>=-1 and tab[0][i][alex]<-0.9999999 and ntm  == 0):
						tab[1][i]=tab[1][alex]
					elif(tab[0][i][alex]==-1 and ntm  != 0):
						tab[1][i]=str(tab[0][i][alex])+tab[1][alex]
					elif (ntm  == 0):
				
						tab[1][i]=str(-(tab[0][i][alex]))+tab[1][alex]
					else:
					
						tab[1][i]=str(tab[1][i])+str(-(tab[0][i][alex]))+tab[1][alex]
				alex+=1  
		i-=1
		col-=1

def Projet(tab):
	tab=pivotGauss(tab)
	if tab!= False:
		remo = remonterGaus(tab)
		Affiche(remo)
		solution(remo)
	else:
		print(False)

def produitAlph(tab,a):
	n=len(tab[0])
	for i in range(n):
		for j in range(n):
			tab[0][i][j]*=a
	return tab

def pertinance(tab,alpha):
	n=len(tab[0])
	e=dict()
	tab=produitAlph(tab,alpha)
	for i in range(n):
		e[i]=dict()
		for j in range(n):

			e[i][j]=(1/n)*0.15*100
			tab[0][i][j]*=100
			tab[0][i][j]+=e[i][j]
			tab[0][i][j]/=100
			
	#return tab

def genererMatrice(n):
	Tab=dict()

	Tab[0]=dict()
	for i in range (0,n):
		Tab[0][i]=dict()

	for i in range(0,n):
		for j in range(0,n):
			if i==j:
				Tab[0][i][j]=0
			else:
				Tab[0][i][j]=randint(0,1)
	Tab[1]=dict()
	for i in range(0,n):
		Tab[1][i]=randint(0,n)
	return Tab

def moinsId(Tab):
	n=len(Tab[0])
	for i in range(n):
		Tab[0][i][i]-=1

def tri(i,j):
	if i>j:
		return 1
	elif i<j:
		return -1
	else:
		return 0

def classement(Tab):
	n=len(Tab[0])
	classemen=dict()
	a=dict()
	for i in range(n):
		classemen[i]=i
		a[i]=(-1)*Tab[0][i][n-1]
	a[i]=1

	for i in range(n):
		for j in range(n):
			if(a[i]>a[j]):
				x=a[j]
				a[j]=a[i]
				a[i]=x
				classemen[i],classemen[j]=classemen[j],classemen[i]

	print('Classement des pages :')
		
	for i in range(len(classemen)):
			print(i,": page ",classemen[i]+1," pertinance = ",a[i])



Tab=dict()

Tab[0]=dict()
for i in range (0,12):
	Tab[0][i]=dict()
	
Tab[0][0][0]=0
Tab[0][0][1]=1/2
Tab[0][0][2]=1/2
Tab[0][0][3]=1/2
Tab[0][0][4]=0
Tab[0][0][5]=1/2
Tab[0][0][6]=0
Tab[0][0][7]=0
Tab[0][0][8]=0
Tab[0][0][9]=0
Tab[0][0][10]=0
Tab[0][0][11]=0

Tab[0][1][0]=1/4
Tab[0][1][1]=0
Tab[0][1][2]=0
Tab[0][1][3]=1/2
Tab[0][1][4]=0
Tab[0][1][5]=0
Tab[0][1][6]=0
Tab[0][1][7]=0
Tab[0][1][8]=0
Tab[0][1][9]=0
Tab[0][1][10]=0
Tab[0][1][11]=0

Tab[0][2][0]=1/4
Tab[0][2][1]=1/2
Tab[0][2][2]=0
Tab[0][2][3]=0
Tab[0][2][4]=0
Tab[0][2][5]=0
Tab[0][2][6]=0
Tab[0][2][7]=0
Tab[0][2][8]=0
Tab[0][2][9]=0
Tab[0][2][10]=0
Tab[0][2][11]=0

Tab[0][3][0]=1/4
Tab[0][3][1]=0
Tab[0][3][2]=1/2
Tab[0][3][3]=0
Tab[0][3][4]=0
Tab[0][3][5]=0
Tab[0][3][6]=0
Tab[0][3][7]=0
Tab[0][3][8]=0
Tab[0][3][9]=0
Tab[0][3][10]=0
Tab[0][3][11]=0

Tab[0][4][0]=1/4
Tab[0][4][1]=0
Tab[0][4][2]=0
Tab[0][4][3]=0
Tab[0][4][4]=0
Tab[0][4][5]=0
Tab[0][4][6]=1
Tab[0][4][7]=0
Tab[0][4][8]=1/4
Tab[0][4][9]=0
Tab[0][4][10]=0
Tab[0][4][11]=0

Tab[0][5][0]=0
Tab[0][5][1]=0
Tab[0][5][2]=0
Tab[0][5][3]=0
Tab[0][5][4]=1/2
Tab[0][5][5]=0
Tab[0][5][6]=0
Tab[0][5][7]=0
Tab[0][5][8]=0
Tab[0][5][9]=0
Tab[0][5][10]=0
Tab[0][5][11]=0

Tab[0][6][0]=0
Tab[0][6][1]=0
Tab[0][6][2]=0
Tab[0][6][3]=0
Tab[0][6][4]=0
Tab[0][6][5]=1/2
Tab[0][6][6]=0
Tab[0][6][7]=1/2
Tab[0][6][8]=0
Tab[0][6][9]=0
Tab[0][6][10]=0
Tab[0][6][11]=0

Tab[0][7][0]=0
Tab[0][7][1]=0
Tab[0][7][2]=0
Tab[0][7][3]=0
Tab[0][7][4]=1/2
Tab[0][7][5]=0
Tab[0][7][6]=0
Tab[0][7][7]=0
Tab[0][7][8]=0
Tab[0][7][9]=0
Tab[0][7][10]=0
Tab[0][7][11]=0

Tab[0][8][0]=0
Tab[0][8][1]=0
Tab[0][8][2]=0
Tab[0][8][3]=0
Tab[0][8][4]=0
Tab[0][8][5]=0
Tab[0][8][6]=0
Tab[0][8][7]=1/2
Tab[0][8][8]=0
Tab[0][8][9]=1/2
Tab[0][8][10]=1/2
Tab[0][8][11]=1/2

Tab[0][9][0]=0
Tab[0][9][1]=0
Tab[0][9][2]=0
Tab[0][9][3]=0
Tab[0][9][4]=0
Tab[0][9][5]=0
Tab[0][9][6]=0
Tab[0][9][7]=0
Tab[0][9][8]=1/4
Tab[0][9][9]=0
Tab[0][9][10]=0
Tab[0][9][11]=1/2

Tab[0][10][0]=0
Tab[0][10][1]=0
Tab[0][10][2]=0
Tab[0][10][3]=0
Tab[0][10][4]=0
Tab[0][10][5]=0
Tab[0][10][6]=0
Tab[0][10][7]=0
Tab[0][10][8]=1/4
Tab[0][10][9]=1/2
Tab[0][10][10]=0
Tab[0][10][11]=0

Tab[0][11][0]=0
Tab[0][11][1]=0
Tab[0][11][2]=0
Tab[0][11][3]=0
Tab[0][11][4]=0
Tab[0][11][5]=0
Tab[0][11][6]=0
Tab[0][11][7]=0
Tab[0][11][8]=1/4
Tab[0][11][9]=0
Tab[0][11][10]=1/2
Tab[0][11][11]=0



Tab[1]=dict()

# Tab[1][5]=0

#Tab=genererMatrice(6)

#Tab=dict()
Tab[0]=creerReseau(30)
for i in range(30):
	Tab[1][i]=0
AfficheReseau(Tab[0])
print("\n")
pertinance(Tab,0.85)
print("\n")
Affiche(Tab)
moinsId(Tab)
print("\n")
AfficheReseau(Tab[0])
print("\n")
Projet(Tab)
classement(Tab)


