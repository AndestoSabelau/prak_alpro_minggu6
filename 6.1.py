def bilprima(a):
    temp=0
    bilprima = [ ]
    for i in range (1, a+1):
        for j in range (1,i+1):
            if i % j == 0:
                temp = temp + 1
        if temp == 2:
            bilprima = bilprima + [i]
            temp = 0
        else:
            temp = 0
    Result = max(bilprima)
    return Result
Num = int(input("masukan angka :"))
print("Bilangan prima terdekat sebelum bilangan",Num,"adalah",bilprima(Num))