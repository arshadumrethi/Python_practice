num = input()
count = 0
for i in range(1, num):
    if num % i == 0:
        count += i
print count
