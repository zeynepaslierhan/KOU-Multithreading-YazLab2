def similarity(X,Y):
    
    X_set=set(X.split())
    Y_set=set(Y.split())

    maxLen=len(Y_set)
    if len(X_set)>len(Y_set):
        maxLen=len(X_set)

    rvector = X_set.union(Y_set)

    similarityValue=0

    Xword=0
    Yword=0

    list_X = X.lower().split()
    list_Y = Y.lower().split()

    words = []
    for w in rvector:
        w=w.lower()

        if words.count(w) != 0:
            continue

        words.append(w)

        Xword=list_X.count(w)
        Yword=list_Y.count(w)
        if (Xword != 0 and Yword != 0):
            if Xword >=Yword:
                similarityValue+=Xword
            else: similarityValue+=Yword

    similarity = (similarityValue/maxLen)*100
    print("similarity: %", similarity)

    return similarity