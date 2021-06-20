


arr = []
arr2 = []
arr3 = []
arr.append("person")
arr.append("person")
arr.append("person")
arr.append("car")
arr.append("person")


file1 = open("labels.txt", 'r')
Lines = file1.readlines()
for line in Lines:
    vline = line.replace("\n","")
    #print(line.replace("\n",""))
    occ = 0
    for ar in arr:
        if (ar == vline):
            occ+=1
    arr2.append(occ)
    arr3.append(vline)
i = -1
for ari in arr2:
    i+=1
    print(ari)
    print("X")
    print(arr3[i])
    print("-----")

