n = int(input('Digite um número: '))
x = 1
print('Essa é a tabuado do número digitado: ')
print('=============')
for x in range(1,11) :
    t = n * x
    print('{:2} x {:2} = {:2}'.format(n, x, t))
    x = x + 1
print('=============')