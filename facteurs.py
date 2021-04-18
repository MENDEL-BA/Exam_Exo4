def facteurs(a):
    resultat = []
    
    for i in range(1,a):
      if a % i == 0 :
        resultat.append(i)
        
    resultat.append(a)
    print("resultat ",resultat)
    return resultat