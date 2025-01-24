N = int(input())
if  not (1 < N < 26):
  print('N должен быть в диапазоне (1, 26)')
else:
  for i in range (N):
    print(chr(65 + i))