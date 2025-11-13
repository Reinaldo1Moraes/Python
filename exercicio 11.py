larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua aréa é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {:.2f}l de tinta.'.format(tinta))