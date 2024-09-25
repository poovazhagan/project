for i in range(1,27):
    if i%2==0:
        print(chr(i+64),chr(96+i))
    else:
        print(chr(i+96),chr(64+i))
