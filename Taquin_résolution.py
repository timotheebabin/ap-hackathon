from juliacall import Main as jl
import numpy as np


#On stocke le taquin sous forme de liste ou de matrice pour la résolution.
#On commence par déterminer si une position est atteignable ou non.

"""
Principe de la fonction : on se convainc facilement, en manipulant le taquin, qu'en déplaçant un numéro,
on le déplace toujours de 0 (mouvement horizontal) ou 2 places (mouvement vertical) dans la liste de 1 à 8.
Par exemple :
1 2 3     1 0 3
4 0 5 --> 4 2 5
7 8 6     7 8 6

revient à passer de la liste [1,2,3,4,5,7,8,6]
à la liste [1,3,4,2,5,7,8,6]
On a déplacé 2 de deux positions.

BREF : on n'effectue JAMAIS une seule transposée (de signature -1), et toujours zéro ou deux (de signature 1)
... il suffit de caculer la signature de la permutation. Si c'est -1, unreachable, si c'est 1, reachable.

Pour une démonstration rigoureuse, euh plus tard
"""

#Cette fonction renvoie un bool indiquant si le board est atteignable.
def is_reachable(given_board):
    assert type(given_board) == np.ndarray or type(given_board)==list, "il faut un tableau numpy ou une liste"
    #on commence par convertir tout cela en un tableau array linéaire de 8 cases
    board = np.array([0 for i in range(8)])
    k=0
    given_board2=given_board.copy() #pour éviter les effets colatéraux
    if type(given_board2) == np.ndarray and given_board2.shape==(3,3) :
        given_board2.reshape(9)
    elif type(given_board2) == list :
        given_board2=np.array(given_board2)
    for i in range(9) :
        a = given_board2[i]
        if a != 0 :
            board[k] = a
            k += 1
    
    #maintenant, on calcule la signature
    #Pour épargner au code des calculs sur des floats, on préfère faire des batteries de test.
    epsilon = 1
    for i in range(1,8) :
        for j in range(i+1,9) :
            sigmai = board[i-1]
            sigmaj = board[j-1]
            if ((i<j and sigmai>sigmaj) or (i>j and sigmai<sigmaj)):
                epsilon *= (-1)
    #On conclut
    if epsilon == 1:
        return True
    else :
        return False
    


#La résolution du taquin est faite en Julia pour réduire le temps de calcul. On effectue un parcours en largeur étant donné que le graphe n'est pas pondéré.

jl.seval('using Revise ; include("BFS.jl")')

def resolution(depart) :
    depart_julia = jl.Vector([depart[i] for i in range(len(depart))])
    chemin_julia = jl.trouve_chemin(jl.map, depart_julia)
    chemin = [np.reshape(np.array(chemin_julia[i]), (3,3)) for i in range(jl.length(chemin_julia))]
    return chemin

print(resolution([1,2,3,4,5,6,7,0,8]))