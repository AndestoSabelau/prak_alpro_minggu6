Height = 5
Wide = 4
Num = int(input("Masukan Angka :"))

for i in range (Height):
    for j in range(Wide):
        Num = Num + 1
        print(f"{Num}\t",end = " ")
    print("")