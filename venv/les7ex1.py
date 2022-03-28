class Matrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in n1])) + '\n'\
               + str('\n'.join(['\t'.join([str(j) for j in i]) for i in n2]))
    def __add__(self):
        mat = [[0, 0],
                [0, 0]]
        for i in range(len(self.a)):
                    for j in range(len(self.b[i])):
                        mat[i][j] = self.a[i][j] + self.b[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))
n1 = [[2, 4],
      [3, 1]]
n2 = [[1, 3],
      [5, 8]]
m1 = Matrix(n1, n2)
print(m1)
print(m1.__add__())

