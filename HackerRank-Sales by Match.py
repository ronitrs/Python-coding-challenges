def sockMerchant(n, ar):
    pairs = 0
    arr = []
    for sock in ar:
        if sock not in arr:
            arr.append(sock)
        elif sock in arr:
            pairs+=1
            arr.remove(sock)
    return pairs
