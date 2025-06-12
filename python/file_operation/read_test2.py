with open("test.txt", "rb") as file:
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    print(f"File size is: {size}")

    file.seek(3, 1)
    piece1 = file.read(4).decode("utf-8")
    print(piece1)

    file.seek(-8, 2)
    piece2 = file.read(8).decode("utf-8")
    print(piece2)