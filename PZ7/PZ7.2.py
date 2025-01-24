N = str(input())
a = ''
b = ''
for i in range(len(N)):
  if (i % 2) == 0:
    a += N[i]
  else:
    b = N[i] + b
c = a + b
print(c)