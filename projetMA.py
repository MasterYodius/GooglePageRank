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

def calculLigne(Tab,pivot,cible):
	coef=Tab[0][cible][pivot]/Tab[0][pivot][pivot]
	for i in range (0,len(Tab[0])):
		Tab[0][cible][i]=int(Tab[0][cible][i] - coef * Tab[0][pivot][i])
		
	Tab[1][cible]=Tab[1][cible] - coef * Tab[1][pivot]
	return Tab
	
def organiser(Tab,pivot):
	
	if Tab[0][pivot][pivot]==0:
		i,n=pivot+1,len(Tab[0])
		while i<n :
			if Tab[0][i][pivot]!=0 :
				Tab=echange(Tab,pivot,i)
				break
			i=i+1
	return Tab

def pivotGauss(Tab):
	
	for i in range(0,len(Tab[0])):
		for j in range(i+1,len(Tab[0])):
			Tab = organiser(Tab,i)
			if(Tab[0][j][i]!=0):
				Tab=calculLigne(Tab,i,j)


	return Tab


def genererMatrice(n):
	Tab=dict()

	Tab[0]=dict()
	for i in range (0,n):
		Tab[0][i]=dict()

	for i in range(0,n):
		for j in range(0,n):
			Tab[0][i][j]=randint(0,1)

	Tab[1]=dict()
	for i in range(0,n):
		Tab[1][i]=randint(0,n)
	return Tab



Tab=dict()

Tab[0]=dict()
for i in range (0,6):
	Tab[0][i]=dict()
	
Tab[0][0][0]=0
Tab[0][0][1]=1
Tab[0][0][2]=0
Tab[0][0][3]=0
Tab[0][0][4]=1
Tab[0][0][5]=1

Tab[0][1][0]=1
Tab[0][1][1]=0
Tab[0][1][2]=0
Tab[0][1][3]=1
Tab[0][1][4]=0
Tab[0][1][5]=0

Tab[0][2][0]=0
Tab[0][2][1]=0
Tab[0][2][2]=1
Tab[0][2][3]=0
Tab[0][2][4]=1
Tab[0][2][5]=0

Tab[0][3][0]=0
Tab[0][3][1]=1
Tab[0][3][2]=0
Tab[0][3][3]=0
Tab[0][3][4]=1
Tab[0][3][5]=1

Tab[0][4][0]=1
Tab[0][4][1]=1
Tab[0][4][2]=1
Tab[0][4][3]=1
Tab[0][4][4]=1
Tab[0][4][5]=1

Tab[0][5][0]=0
Tab[0][5][1]=0
Tab[0][5][2]=1
Tab[0][5][3]=0
Tab[0][5][4]=0
Tab[0][5][5]=1


Tab[1]=dict()
Tab[1][0]=1
Tab[1][1]=0
Tab[1][2]=4
Tab[1][3]=4
Tab[1][4]=4
Tab[1][5]=2

Tab=genererMatrice(20)
Affiche(Tab)
print("")
 #echange retourne 2 valeur qu on met dans une nouvelle variable de matrice et X
Tab=pivotGauss(Tab)
Affiche(Tab)
