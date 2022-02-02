def tri_rapide(tableau):
    if not tableau:
            return []
    else:
        for i in range(len(tableau)-1,0,-1):
            for j in range(i):
                if tableau[j][1]<tableau[j+1][1]:
                    tableau[j+1], tableau[j] = tableau[j], tableau[j+1]

    return tableau    
            
def max_username_length(tableau):
    if not tableau:
            return 0

    else:
        max=len(tableau[0][0])
        for i in range(1,len(tableau),1):
            if (max<len(tableau[i][0])):
                max=len(tableau[i][0])

            
    
    return max 


def normalize_username(tableau,max):

    for i in range(len(tableau)):
        user = tableau[i][0]
        score = tableau[i][1]
        
        nb_space = max - len(user)
        if (score<1000):
            nb_space+=1
        user += " "*nb_space
        tableau[i][0]=user
        
    return tableau
        


        
        