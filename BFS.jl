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




function bfs(start, goal)
    #Initialisation de la carte des distances sous forme de dictionnaire.
    map = Dict{Vector{Int}, Tuple{Int, Vector{Int}}}()
    map[start]  = 0


    #Initialisation de la file de priorité
    tas = [start]
    for summit in neighbors(start)
        push!(tas, 1)
    end

    #Etapes
    summit = start
    while summit != goal
        
        
        #Sélection du k-ième sommet le plus proche de s0
        (w,i) = pop!(tas)
        while (length(tas.data) > 0) && (i in keys(map)) 
            (w,i) = pop!(tas)
        end
        map[i] = w

        #Ajout de nouveaux chemins dans le tas.
        for t in g.neighbors 
            s, j, w_2 = t
            if (s == i) && ~ (j in keys(map))
                push!(tas, (w_2 + w, j))
            end
        end

        k+=1
    end

    map
end
