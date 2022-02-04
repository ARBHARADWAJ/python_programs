t=int(input())
for _ in range(t):
    l,m=map(int,input().split())
    tb=0
    tl=0
    c=0
    while tl<=l and tb<=m:
       c=c+1 
       tl=tl+c
       c=c+1
       tb=tb+c
    if tl>l and tb>m:
        print("Bob")
    elif tl>l:
        print("Bob")
    else:
        print("Limak")