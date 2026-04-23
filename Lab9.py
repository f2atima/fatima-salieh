import numpy as np

A = np.arange(1, 21).reshape(4, 5)
print(A)
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.itemsize)

B = A.reshape(5, 4)
print(B)

import numpy as np
a=np.array([0.,0.,0.],
[10.,10.,10.],
[20.,20.,20.],
[30.,30.,30.],)
b=np.array([0.,1.,2],)

b = np.array([0,1,2,1])

c = a + b
print(c)

mask = c >= 22
print(mask)
print(np.sum(mask))

grades = np.array([[87,96,70],
                   [100,87,90],
                   [94,77,90],
                   [100,81,82]])

print(np.sum(grades))
print(np.min(grades))
print(np.max(grades))
print(np.mean(grades))
print(np.std(grades))
print(np.var(grades))

print(np.mean(grades, axis=0))
print(np.mean(grades, axis=1))
print(np.max(grades, axis=1))

arr = np.array([[2,4,6],
                [1,3,5],
                [7,9,11]])

print(np.sum(arr, axis=1))
print(np.sum(arr, axis=0))
print(np.mean(arr))

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

v = np.array([2,4])

print(A * B)
print(A @ B)
print(A * v)

B = np.array([1,2,3])
A = np.array([[1,2,3],
              [4,5,6]])

print(A + B)
print(A * 2)
print(A - 5)

grades = np.array([[70,85,90],
                   [88,76,95],
                   [60,80,72]])

print(np.unravel_index(np.argmax(grades), grades.shape))
print(np.argmax(grades, axis=1))
print(np.argmin(grades, axis=1))

np.random.seed(0)
matrix = np.random.randint(-5,6,(4,4))
print(matrix)

values, counts = np.unique(matrix, return_counts=True)
print(values)
print(counts)

print(np.unique(matrix, axis=0))

a = np.array([[1,0,0],
              [1,0,0],
              [2,3,4]])

print(np.unique(a, axis=0))

x = np.array([2,0,1,5,4,1,9])
A = np.array([[3,8,1],
              [6,2,9]])

ind = np.argsort(x)
print(x[ind])

print(np.unravel_index(np.argmin(A), A.shape))

print(np.where(x >= 3))

print(np.split(x, [2,5]))

table = np.array([
    [5,8,2,7],
    [1,9,4,3],
    [6,0,11,10],
    [12,13,14,15]
])

print(table[1])
print(table[:,2])
print(table[1:3,1:3])

scores = np.array([
    [70,80,90],
    [60,75,85],
    [88,92,79],
    [55,65,72]
])

scores = scores + 5
print(scores)

scores[0] = [100,100,100]
print(scores)

scores[:,2] = 0
print(scores)