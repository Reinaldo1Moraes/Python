peso = float(input('Qual é o peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('PARABENS! Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está acima do peso se cuide')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MORBIDA tome cuidado...')



