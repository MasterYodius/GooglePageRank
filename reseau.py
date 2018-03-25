
from random import * 
def creerReseau(n):# 2n² + n
	Tab=dict()
	for i in range (n):
		Tab[i]=dict()

	for j in range(n):
		count=0
		for i in range(n):
			if i==j:
				Tab[i][j]=-1
			else:
				Tab[i][j]=randint(0,1)
				if Tab[i][j]==1:
					count+=1
		if count!=0:
			for i in range(n):
				if Tab[i][j]==1:
					Tab[i][j]/=count
		else:
			for i in range(n):
				Tab[i][j]+=1/n

	return Tab

def AfficheReseau(Tab) : # n²
	
	i=0
	n=len(Tab)
	while i<n:
		j=0
		print("| ",end='')
		while j<n:
			print(Tab[i][j],end='  |')
			j=j+1
		print("")
		i=i+1

#AfficheReseau(creerReseau(5)) #3*10000²+10000