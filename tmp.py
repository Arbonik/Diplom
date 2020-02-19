import random
name = 'Bob'
age = 14

n = int(input())
m = int(input())
array = [[random.randint(0, 100) for i in range(n)] for j in range(m)]

for i in range(0, m):
    for j in range(0, n):
        print(array[i][j], end=' ')
    print()

sum = [0] * m

for i in range(0, m ):
    for j in range(0, n):
        sum[i] += array[i][j]

print('name:', name, 'age', age, sep='@@@', end=' ')
print('name: %s age %d' % (name, age))
print('name: {} age {:$=5}'.format(name, age))
print(f'name: {name} \nage {age:$=5} {3 / 34}')