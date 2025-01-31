function convertit_position_2D(n)
    ((n-1)÷3 +1), ((n-1)%3 +1)
end

function convertit_position_1D(i,j)
    (i-1)*3 + j
end

function echange_sommets(summit, pos_zero, new_n)
    summit[new_n], summit[pos_zero] = 0, summit[new_n]
    summit, new_n
end

function neighbors(summit, pos_zero)
    i,j = convertit_position_2D(pos_zero)
    voisins = Tuple{Vector{Int}, Int}[]
    if i < 3 
        new_n = convertit_position_1D(new_i,new_j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, new_n))
    end
    if j < 3 
        new_n = convertit_position_1D(new_i,new_j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, (i,j+1)))
    end
    if i > 1 
        new_n = convertit_position_1D(new_i,new_j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, (i-1,j)))
    end
    if j > 1 
        new_n = convertit_position_1D(new_i,new_j)
        push!(voisins, echange_sommets(copy(summit), pos_zero, (i,j-1)))
    end
    voisins
end


function bfs(goal)
    #Initialisation de la carte des distances sous forme de dictionnaire.
    map = Dict{Vector{Int}, Tuple{Int, Vector{Int}}}() 
    #chaque valeur du dictionnaire est un tuple représentant la distance à l'arrivée et le prédécesseur dans le chemin
    map[goal]  = (0, Int[]) #le sommet de départ n'a pas de parent 


    #Initialisation de la liste des sommets à visiter
    a_visiter = Tuple{Vector{Int}, Int}[] #on met dans la file à visiter : le taquin, la position du zéro et son prédécesseur
    for voisin in neighbors(goal, 9)
        summit, _ = voisin
        push!(a_visiter, voisin) 
        map[summit] = (1, start)
    end

    #Etapes
    summit = goal
    while !isempty(a_visiter)
        (summit, pos_zero) = popfirst!(a_visiter)
        for voisin in neighbors(summit, pos_zero)
            s, _ = voisin
                if not s in keys(map)
                    map[s] = (map[summit][1]+1, summit)
                    push!(a_visiter, voisin)
                end
        end
    end
    map
end

function trouve_chemin(map, start)
end
