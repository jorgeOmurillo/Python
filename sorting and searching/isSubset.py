def isSubset(A, B):
    return set(A).issubset(B)

print(isSubset(['A','B','C','D','E'], ['A','E','D']))
print(isSubset(['A','D','E'], ['A','A','D','E']))
