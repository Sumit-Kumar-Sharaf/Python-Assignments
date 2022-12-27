"""Write a python program to create a dictionary that
contains three dictionaries (nested)"""

detail={17:{"Name":"Sumit Sharaf","College":"S.R.K.G"},
18:{"Name":"Saroj","College":"S.R.K.G"},
16:{"Name":"Sushil","College":"S.R.K.G"}}
for k in detail:
    for e in detail[k]:
        print(k,end=" ")
        print(e,(detail[k])[e],end=" ")
    print("")