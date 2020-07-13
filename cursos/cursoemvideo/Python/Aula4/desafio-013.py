sal = float(input('Digite o valor do salario: '))
alm = sal * (15/100)
som = sal + alm
print('O valor atual do salario é R$ {:.2f}, vai ter um almento de R$ {:.2f} e vai para R$ {:.2f}'.format(sal, alm, som))