from random import * 

def Affiche(Tab) :
	
	i=0
	n=len(Tab[0])
	while i<n:
		j=0
		print("| ",end='')
		while j<n:
			print(Tab[0][i][j],end='  ')
			j=j+1
		print("| ",Tab[1][i]," |\n")
		i=i+1


def echange(Tab,l1,l2):
	for i in range (0,len(Tab[0])):
		Tab[0][l1][i],Tab[0][l2][i]=Tab[0][l2][i],Tab[0][l1][i]
		
	Tab[1][l1],Tab[1][l2]=Tab[1][l2],Tab[1][l1]
	return Tab

def calculLigne(Tab,pivot,cible,colonne):

	coef=Tab[0][cible][colonne]/Tab[0][pivot][colonne]
	for i in range (0,len(Tab[0])):
		Tab[0][cible][i]=int(Tab[0][cible][i] - coef * Tab[0][pivot][i])
		
	Tab[1][cible]=int(Tab[1][cible] - coef * Tab[1][pivot])
	return Tab
	
def organiser(Tab,pivot):
	
	k=0
	while pivot+k < len(Tab[0]):
		if Tab[0][pivot][pivot+k]==0:
			i,n=pivot+1,len(Tab[0])
			while i<n :
				if Tab[0][i][pivot+k]!=0 :
					Tab=echange(Tab,pivot,i)
					return Tab
				i=i+1
		k+=1
		print(pivot+k)
	return Tab

def pivotGauss(Tab):
	n=len(Tab[0])
	colonne = 0
	for i in range(0,n):
		if Tab[0][i][colonne]==0:

			#print(i,colonne,"1")
			#Affiche(Tab)
			Tab = organiser(Tab,i)
			#print(i,colonne,"2")
			#Affiche(Tab)

		if Tab[0][i][colonne]==0:
			colonne+=1

		for j in range(i+1,n): #boucle pour calculer les lignes en dessous 
			
			if(Tab[0][j][colonne]!=0):
				Tab=calculLigne(Tab,i,j,colonne)

		colonne+=1
		if colonne==n:
			break

	for i in range(0,n):
		if(Tab[0][i][i]<0):
			k=Tab[0][i][i]
			for j in range(i,n):
				Tab[0][i][j]=int(Tab[0][i][j]/k)
			Tab[1][i]=int(Tab[1][i]/k)
	return Tab

"""	if(SiSolution(Tab)):
		i=n
		while i>0:
			for j in range():
			i-=1
"""
def SiSolution(Tab):
	n=len(Tab[0])
	
	for i in range (0,n):
		retour=False
		for j in range(0,n):
			if(Tab[0][i][j]!=0):
				retour=True
		if(retour==False and Tab[1][i]!=0):
			return False




	return True



"""def gausJordan(tab):
	r=0
	m=len(tab[1])
	for j in range 0,m:
"""





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
				Tab[0][i][j]=randint(0,n)
	Tab[1]=dict()
	for i in range(0,n):
		Tab[1][i]=randint(0,n)
	return Tab



Tab=dict()

Tab[0]=dict()
for i in range (0,3):
	Tab[0][i]=dict()
	
Tab[0][0][0]=1
Tab[0][0][1]=-1
Tab[0][0][2]=-4
"""Tab[0][0][3]=0
Tab[0][0][4]=0
Tab[0][0][5]=1
"""
Tab[0][1][0]=2
Tab[0][1][1]=-3
Tab[0][1][2]=4
"""Tab[0][1][3]=1
Tab[0][1][4]=0
Tab[0][1][5]=1
"""
Tab[0][2][0]=0
Tab[0][2][1]=2
Tab[0][2][2]=8
"""
Tab[0][2][3]=0
Tab[0][2][4]=1
Tab[0][2][5]=0"""
"""
Tab[0][3][0]=0
Tab[0][3][1]=0
Tab[0][3][2]=1
Tab[0][3][3]=0
Tab[0][3][4]=0
Tab[0][3][5]=1

Tab[0][4][0]=0
Tab[0][4][1]=0
Tab[0][4][2]=1
Tab[0][4][3]=1
Tab[0][4][4]=0
Tab[0][4][5]=1

Tab[0][5][0]=1
Tab[0][5][1]=1
Tab[0][5][2]=1
Tab[0][5][3]=0
Tab[0][5][4]=1
Tab[0][5][5]=0
"""

Tab[1]=dict()
Tab[1][0]=3
Tab[1][1]=14
Tab[1][2]=0
"""Tab[1][3]=3
Tab[1][4]=3
Tab[1][5]=3
"""

#Tab=genererMatrice(20)
Affiche(Tab)
print("")
Tab=pivotGauss(Tab)
print("")
Affiche(Tab)
print(SiSolution(Tab))
