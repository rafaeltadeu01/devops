## Calculadora de utilização de tinta em litros
aut = float(input('Qual é a altura da parede: '))
lag = float(input('Qual é a largura da parede: '))
area = aut*lag
tinta = area / 2
print('A parede tem a dimensões de {:.1f} x {:.1f} e sua area tem {:.1f}m²'.format(aut, lag, area))
print('Para pintar a parede serão necessario {:.0f}L de tinta'.format(tinta))