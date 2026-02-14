sum1 = 0
i = 0

while i < 10:
    num = int(input("Enter number: "))

    if num == 0:
        break

    if num < 0:
        continue

    sum1 += num
    i += 1

print("Sum =", sum1)



n = int(input("Enter number: "))

for i in range(1, 13):
    result = n * i

    if result % 3 == 0:
        continue

    if result > 50:
        break

    print(n, "*", i, "=", result)



secret = 12
tries = 0

while True:
    guess = int(input("Guess number (1-20): "))

    if guess < 1 or guess > 20:
        continue

    tries += 1

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong")

print("Attempts =", tries)


 
x = int(input("Enter number: "))
count = 0

for i in range(1, x + 1):

    if i > 50:
        break

    if i % 8 == 0:
        continue

    if i % 4 == 0:
        count += 1

print("Count =", count)


 
for i in range(1, 6):
    for j in range(1, i + 1):

        if j == 3:
            continue

        if i * j > 6:
            break

        print(j, end="")

    print()