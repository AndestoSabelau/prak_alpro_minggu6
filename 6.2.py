def barisan (n):
    temp = 1

    for i in range (1,n+1):
        temp *= i
        return (temp)

n = int(input("masukan angka: "))

for i in range (n,0,-1):
    print(barisan(i),end=" ")
    for j in range (i,0,-1):
        print(j,end=" ")
    print(" ")