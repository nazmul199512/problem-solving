a, b, c, d = [int(input()) for i in range(4)]
print([[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if (i + j + k) != d])
