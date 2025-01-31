from juliacall import Main as jl
import numpy as np
jl.seval('using Revise ; include("BFS.jl") ; map')
#print([np.array(jl.tab[i]) for i in range(jl.length(jl.tab))])
j = jl.seval('d = Dict{Vector{Int}, Int}() ; d[[4,5]] = 5')
print(j)