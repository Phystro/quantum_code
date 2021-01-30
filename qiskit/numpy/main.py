import numpy as np

ar_1 = np.array([1, 2, 3, 4j])

ar_2 = np.array([[1, 2, 3], [4, 5, 6]])

# print(ar_1)
# print(ar_2)

# shape of vector or matrix
print(ar_1.shape)
print(ar_2.shape)

a = np.array([[1, 0]])
b = np.array([[0, 1]])

print(np.array([1, 2]))     # explicit row array
print(np.array([[1], [2]]))     # explicit column array

m = 1/np.sqrt(2)


c = m*(a+b)
d = m*(a-b)


print(c, "\n", d)

# Transpose
print(a)
print(a.T)
print(np.transpose(a))


print(ar_1)
print(ar_1.conj())


# multiplication with arrays
print( a @ b.T )


# defining regularly spaced arrays
zer = np.zeros((4, 5))
one = np.ones((3, 4))
pip = np.full((3, 3), np.pi)
print(zer)
print(one)
print(pip)


print( np.linspace(1, 20, 5) )
print( np.arange(2, 20, 2) )
