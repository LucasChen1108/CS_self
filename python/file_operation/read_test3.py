with open("test.txt", "rb+") as f:
    #get the size first
    f.seek(0, 2)
    size = f.tell()
    f.seek(0,0)

    #read and print the original text
    content = f.read().decode("utf-8")
    print(content)
    print()

    f.seek(15, 0)
    f.write("NEW_TEXT".encode("utf-8"))
    f.flush()

    f.seek(0)
    content = f.read().decode("utf-8")
    print(content)
    print()

    

