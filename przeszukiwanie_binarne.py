L = [1,2,3,4,5,6,7,8]
szukana = 6
dl = (len(L))//2
if L[dl] > szukana:
    dl = dl //2
    print(L[dl])
else:
    dl = (dl + len(L) )//2
    print(dl)
