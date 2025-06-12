my_list = ["Testing", 1, 3.44]
size = 3
def print_list(size, list = []):
    for i in range(size):
        print(list[i], end=' ')
    print('\n')

print_list(3, my_list)

new = input("what do u want to add: ")
my_list.append(new)
size += 1

print("New list")
print_list(size, my_list)
    
