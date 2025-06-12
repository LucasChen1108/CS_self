
with open("test.txt", "r+") as file:
    print(f"cursor's starting point: {file.tell()}")

    line = file.readline()
    print(line)

    print(f"after reading one line, the cursor is at: {file.tell()}")
    file.seek(0)
    line = file.readline()
    print(f"read the first line again: {line}")

