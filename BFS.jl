"""
    convertit_position_2D(n)

Trouve l'indice (i,j) dans une matrice 3*3 de l'élément à la position n dans un vecteur de taille 9.
"""
function convertit_position_2D(n)
    ((n-1)÷3 +1), ((n-1)%3 +1)
end

"""
    convertit_position_1D(i,j)

Trouve l'indice n dans un vecteur de taille 9 de l'élément à la position (i,j) dans une matrice 3*3.
"""
function convertit_position_1D(i,j)
    (i-1)*3 + j
end

"""
    echange_sommets(summit, pos_zero, new_n)

Echange les éléments des sommets pos_zero et new_n dans le vecteur summit.
"""
function echange_sommets(summit, pos_zero, new_n)
    summit[new_n], summit[pos_zero] = 0, summit[new_n]
    summit, new_n
end


"""
    neighbors(summit, pos_zero)

Renvoie la liste des sommets accessibles depuis la position summit, ainsi que la position du 0 dans ces sommets.
"""
function neighbors(summit, pos_zero)
    i,j = convertit_position_2D(pos_zero)
    voisins = Tuple{Vector{Int}, Int}[]
    #Il y a au plus 4 voisins accessibles en fonction de la position du zéro dans le taquin. La position étant stockée sous forme de liste, on calcule les indices correspondants dans la matrice.
    if i < 3 
        new_n = convertit_position_1D(i+1,j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, new_n))
    end
    if j < 3 
        new_n = convertit_position_1D(i,j+1)
        push!(voisins, echange_sommets(copy(summit), pos_zero, new_n))
    end
    if i > 1 
        new_n = convertit_position_1D(i-1,j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, new_n))
    end
    if j > 1 
        new_n = convertit_position_1D(i,j-1)
        push!(voisins, echange_sommets(copy(summit), pos_zero, new_n))
    end
    voisins
end

"""
    bfs(goal)

Effectue un parcours en largeur à partir de l'arrivée. 
Parcourt l'ensemble des positions atteignables depuis l'arrivée, et renvoie un dictionnaire dont les clés sont les positions du tableau accessibles,
et les valeurs sont un tuple comportant leur distance à l'arrivée et leur prédécesseur dans le plus court chemin entre la position et l'arrivée.
"""
function bfs(goal)
    #Initialisation de la carte des distances sous forme de dictionnaire.
    map = Dict{Vector{Int}, Tuple{Int, Vector{Int}}}() 
    #chaque valeur du dictionnaire est un tuple représentant la distance à l'arrivée et le prédécesseur dans le chemin
    map[goal]  = (0, Int[]) #le sommet de départ n'a pas de prédécesseur


    #Initialisation de la liste des sommets à visiter
    a_visiter = Tuple{Vector{Int}, Int}[] #on met dans la file à visiter la disposition du taquin et la position du zéro
    for voisin in neighbors(goal, 9)
        summit, _ = voisin
        push!(a_visiter, voisin) 
        map[summit] = (1, goal)
    end

    #Parcours en largeur
    summit = goal
    while !isempty(a_visiter)
        (summit, pos_zero) = popfirst!(a_visiter)
        for voisin in neighbors(summit, pos_zero)
            s, _ = voisin
                if ~(s in keys(map))
                    map[s] = (map[summit][1]+1, summit)
                    #La distance à l'arrivée du sommet est celle de son prédécesseur +1
                    push!(a_visiter, voisin)
                end
        end
    end
    map
end

"""
    trouve_chemin(map, start)

Renvoie le chemin entre la position start et l'arrivée s'il existe.
"""
function trouve_chemin(map, start)
    summit = start
    path = [start]
    #On parcourt les prédécesseurs jusqu'à arriver à l'objectif.
    while !iszero(map[summit][1])
        summit = map[summit][2]
        push!(path, summit)
    end
    path
end

#Parcours du graphe
arrivee = [1,2,3,4,5,6,7,8,0]
map = bfs(arrivee)

#Tests
using Test
@test_broken trouve_chemin(map, [1,4,2,3,8,5,6,0,7]) #Nous avons vérifié que cette position n'est pas atteignable depuis l'arrivée grâce à la fonction is_reachable
@test trouve_chemin(map, [1,2,3,4,5,0,7,8,6]) == [[1,2,3,4,5,0,7,8,6],[1,2,3,4,5,6,7,8,0]]
