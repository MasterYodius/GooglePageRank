from random import * 

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
		print("i",i,", colonne",colonne, " valeur ",tab[0][i][colonne])
		Affiche(Tab)
		if tab[0][i][colonne] > -0.000000000001 and tab[0][i][colonne] < 0.000000000001:
			tab[0][i][colonne]=0
		if tab[0][i][colonne]!=0: #division 
			coef=tab[0][i][colonne]
			
			for alex in range(i,n):
				tab[0][i][alex]/=coef
			tab[1][i]/=coef				
			#Affiche(tab)	
			#tab[1][i]/=tab[0][i][colonne]
			#tab[0][i][colonne]/=tab[0][i][colonne]
			ligne=1
			while ligne <= i:#soustration
				
				coef=-1*tab[0][i-ligne][colonne]
				#print("coef=",coef)
				alex=n-1
				while alex>i-1:
					#print("cible",tab[0][i-ligne][alex],"pivot",tab[0][i][alex],"avant")
					#Affiche(tab)
					
					tab[0][i-ligne][alex]+=tab[0][i][alex]*coef
					
					#print("cible",tab[0][i-ligne][alex],"pivot",tab[0][i][alex],"apres")
					
					alex-=1
				tab[1][i-ligne]+=tab[1][i]*coef
	#			tab[0][i-ligne][colonne]-=tab[0][i-ligne][colonne]*tab[0][i][colonne]

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
		#if tab[1][i]===(float)tab[1][i] or tab[1][i]===(int)tab[1][i]:

		if isinstance(tab[1][i],float) or isinstance(tab[1][i],int):
			ntm =tab[1][i]
			tab[1][i]=str(tab[1][i])
			alex=col+1
			while alex<=n-1:
				if(tab[0][i][alex]!=0):
					if(tab[0][i][alex]==-1 and ntm  == 0):
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
	print(tab[1])
		

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



Tab=dict()

Tab[0]=dict()
for i in range (0,5):
	Tab[0][i]=dict()
	
Tab[0][0][0]=-1
Tab[0][0][1]=1/4
Tab[0][0][2]=1/4
Tab[0][0][3]=1/4
Tab[0][0][4]=1/4
# Tab[0][0][5]=1

Tab[0][1][0]=0
Tab[0][1][1]=-1
Tab[0][1][2]=1/3
Tab[0][1][3]=1/3
Tab[0][1][4]=1/3
# Tab[0][1][5]=0

Tab[0][2][0]=0
Tab[0][2][1]=0
Tab[0][2][2]=-1
Tab[0][2][3]=0
Tab[0][2][4]=1
# Tab[0][2][5]=1

Tab[0][3][0]=0
Tab[0][3][1]=1/2
Tab[0][3][2]=1/2
Tab[0][3][3]=-1
Tab[0][3][4]=0
# Tab[0][3][5]=0

Tab[0][4][0]=1/3
Tab[0][4][1]=1/3
Tab[0][4][2]=0
Tab[0][4][3]=1/3
Tab[0][4][4]=-1
# Tab[0][4][5]=1

# Tab[0][5][0]=0
# Tab[0][5][1]=0
# Tab[0][5][2]=1
# Tab[0][5][3]=0
# Tab[0][5][4]=1
# Tab[0][5][5]=0


Tab[1]=dict()
Tab[1][0]=0
Tab[1][1]=0
Tab[1][2]=0
Tab[1][3]=0
Tab[1][4]=0
# Tab[1][5]=0

#Tab=genererMatrice(6)
Affiche(Tab)
print("")
Tab=pivotGauss(Tab)
if Tab==False:
	print(Tab)
else:
	Affiche(Tab)
	print("")
	Tab=remonterGaus(Tab)
	Affiche(Tab)
	solution(Tab)

