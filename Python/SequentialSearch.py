def search(array, value):
    for item in array:
        if item == value:
            return item;
    return False

n = int(input("Enter the array size: "))
array = [];
print("Enter the elements:")
for i in range(n):
    num = input()
    array.append(object)
value = input("Enter item for search:")
present = search(array, value)
if present:
    print("Item is found.")
else:
    print("Item is not found.")