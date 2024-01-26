a = 'A'
b = 'B'
c = 1.1

string = 'a={param1} b={param2} c={param3:.2f}'
formato = string.format(
  param1 = a, param2 = b, param3 = c
  )

print(formato)