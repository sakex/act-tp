import random

def inside(point):#Point définit sous la forme d'un tuple
    # Cette fonction permet de vérifier si un point se trouve à l'intérieur ou sur le cercle
    if (point[0]**2+point[1]**2) <= 1:
        return 1
    
    else: 
        return 0
    
def app():
    count = 0 #On initialise le nombre de points dans le cercle
    iter = 10000 # Plus cette valeur augmente, plus on se rapproche de la valeur de pi
    for i in range(iter):
        temp1 = random.random()#Génère la première coordonnée
        temp2 = random.random()#Génère la deuxième coordonnée
        temp = (temp1,temp2)#Crée le point

        count += inside(temp)#On appelle la fonction. Si le point est dans le cercle, elle retourne 1, par conséquent on ajoute 1 au compteur. Sinon elle retourne 0, on ajoute donc rien.
    
    return count/iter*4#Retourne selon la formule donnée dans l'exercice.

print("L'approximation du chiffre pi est : {}".format(app()))