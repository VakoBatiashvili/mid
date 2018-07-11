from string import ascii_lowercase as al
dashifruli=list(input("sheiyvanet dashifruli sityva"))
for i in range(0,26):
    x=""
    for m in dashifruli:
        ind=al.index(m)+i
        if ind>25:
            ind-=25
        
        x+=al[ind]
    print(x,i+1)
            
