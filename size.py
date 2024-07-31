import sys
x = 10
y = "10"
z = 2.13
w = 3 + 5j

print(hex(id(x)))
size_x = sys.getsizeof(x)
print(size_x)

print(hex(id(y)))
size_y = sys.getsizeof(y)
print(size_y)

print(hex(id(z)))
size_z = sys.getsizeof(z)
print(size_z)

print(hex(id(w)))
size_w = sys.getsizeof(w)
print(size_w)
