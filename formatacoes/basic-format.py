"""
Formatação básica
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(<>^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes do zero
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variabel = 'ABC'
print(f'{variabel}')
print(f'{variabel:>10}.')
print(f'{variabel:-<10}.')
print(f'{variabel:^10}.')
print(f'{1000.748384737322334:0=+10,.1f}')