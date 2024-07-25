numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    flag = True
    for j in range(2, i):
        if 1 % j == 0:

            not_primes.append(i)

            #flag = False

            break

    if i not in not_primes:
        primes.append(i)

    #if flag:
        #primes.append(i)
    #else:
        #not_primes.append(i)
print(*primes)
print(*not_primes)

