import random

def gen_pref(n):
    if not isinstance(n, int):
        raise TypeError(f"Le paramètre n doit être un entier, pas un {type(n).__name__}")
    
    if n<=0:
        raise ValueError(f"Le nombre n doit être strictement positif (n>0)")
    
    students=[]
    establishments=[]
    perm=[i for i in range(0,n)]
    for i in range(n):

        random.shuffle(perm)
        students.append(perm.copy())


        random.shuffle(perm)
        establishments.append(perm.copy())
    
    return students,establishments

def print_pref(students,establishments):
    for i in range(len(students)):
        print(f"Student({i}): {students[i]}")
    for i in range(len(establishments)):
        print(f"School({i}): {establishments[i]}")
