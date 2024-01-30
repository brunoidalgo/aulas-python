"""

Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""
name = 'Bruno'
price = 1000.95897643
variable = '%s, this price is $%.2f' % (name, price) # Bruno, this price is $1000.96
print(variable)
print('The hexadecimal of %d at is %04x' % (15,15)) # The hexadecimal of 15 at is 000f