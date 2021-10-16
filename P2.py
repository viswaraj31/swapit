def myswap() : 
    f1n = input("Enter First File Name ")
    f2n = input("Enter second file name ")

    f1r = open(f1n)
    f2r = open(f2n)
    data1 = f1r.read()
    data2 = f2r.read()
    with open("F1.txt","w") as f1w :
        f1w.write(data2)

    with open("F2.txt","w") as f2w :
        f2w.write(data1)

    print("The files have been swapped time for you to run")

myswap()