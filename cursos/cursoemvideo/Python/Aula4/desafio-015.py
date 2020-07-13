## Calculadora de valor da locação de um carro
dias = int(input('Quantos dias ficou alugado?: '))
km = float(input('Quantos KM foi rodados?: '))
pago1 = dias * 60
pago2 = km * 0.15
print('O total a pagar de dias é de: R$ {:.2f}'.format(pago1))
print('O total a pagar de km é de: R$ {:.2f}'.format(pago2))
print('-' * 50)
print('O total do aluguel foi de: R$ {:.2f}'.format(pago1+pago2))