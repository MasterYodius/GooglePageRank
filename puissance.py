from math import sqrt
from reseau import creerReseau
from reseau import AfficheReseau

def produitAlph(tab,a):
	n=len(tab)
	for i in range(n):
		for j in range(n):
			tab[i][j]*=a
	return tab
def produitVecteur(v1,a):
	n=len(v1)
	v=dict()
	for i in range(n):
		v[i]=v1[i]*a
	return v

def moduleS(v1,v2):
	n=len(v1)
	v3=dict()
	res=0

	if(v2==0):
		for i in range(n):
			res+=v1[i]**2
		return sqrt(res)



	for i in range(n):

		v3[i]=v1[i]-v2[i]
		res+=v3[i]**2
	return sqrt(res)

def produitMatrice(A,v):
	v1=dict()
	n=len(A)
	for i in range(n):
		v1[i]=0
		for j in range(n):
			v1[i]+=A[i][j]*v[j]
	return v1
def copie(x1,x2):
	n=len(x1)
	for i in range(n):
		x1[i]=x2[i]
	return x1
def puissance(A,imax,E):
	n=len(A)
	Xo=dict()
	for i in range(n):
		Xo[i]=1/sqrt(n)
	k=1
	Yk=produitMatrice(A,Xo)
	Xk=produitVecteur(Yk,1/moduleS(Yk,0))


	while k<=imax and moduleS(Xo,Xk) <= E:
		Xo=copie(Xo,Xk)
		Yk=produitMatrice(A,Xo)
		Xk=produitVecteur(Yk,1/moduleS(Yk,0))
		k+=1

	return moduleS(Yk,0)



A=creerReseau(5)
AfficheReseau(A)
print(puissance(A,5000,1))
