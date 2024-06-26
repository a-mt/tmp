
for i in range(0,11):
    if i % 2 == 0:
        print(i)

for i in range(0,10):
    if i % 2 != 0:
        print(i)

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
n_positif = 0
for item in liste:
    print("-", item)
    if item > 0:
        n_positif += 1
print("# positif:", n_positif)