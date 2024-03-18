'''
if kondisi1:
    if kondisi2:
        s
        s
    else:
        s
        s 
else:
    if kondisi3:
        s
        s
    else:
        s
        s
S

if kondisi1:
    if kondisi2:
        if kondisi3:
            if kondisi4:
                s

if kondisi1:
    S
else:
    if kondisi2:
        S
    else:
        if kondisi4:
            S
'''
for i in range (7):
    print(i, end= " ")
    if i == 5:
        continue