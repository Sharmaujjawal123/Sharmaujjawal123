for i in range(1,3):
    print("i=", i)
    for j in range(1,i+1):
        print("j in loop=",j)

        for k in range(1,j+1):
            print("k=", k)
        print("i=",i,"j=",j,"k=",k)