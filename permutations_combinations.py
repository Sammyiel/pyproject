# This python program would produce the r-permutations
# and the r-combinations

# Importing modules
from itertools import permutations
from itertools import combinations

lst = []

while True:
    try:
        n = lst.append(int(input("Add a value to a list of values to be chosen from: ")))

    except:
        print("Enter numeric values")

    add = input("Do you want to add to list (yes/no)? ")
    if 'y' in add:
        continue
    else:
        break

r = int(input("Enter the value r\nr must not exceed the number of items in your list: "))

print("\nYour list:")
print(lst)

# Print the obtained permutations
perm = permutations(lst, r)
print("\nThese are the permutations:")
count_perm = 0
for i in list(perm):
    count_perm = count_perm + 1
    print(i)

print(str(count_perm) + " permutations computed successfully")
# Print the obtained combinations
comb = combinations(lst, r)
print("\nThese are the combinations:")
count_comb = 0
for i in list(comb):
    count_comb = count_comb + 1
    print(i)

print(str(count_comb) + " combinations computed successfully")
