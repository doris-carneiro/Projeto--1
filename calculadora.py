num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operation = input('''
Digite a operação matemática que gostaria de realizar:
a para adição
b para subtração
c para multiplicação
d para divisão
''')

if operation == 'a':
  print("A soma dos 2 números é: ", num1 + num2)

elif operation == 'b':
  print("A subtração entre os 2 números é: ", num1 - num2)

elif operation == 'c':
  print("A multiplicação entre os 2 números é: ", num1 * num2)

elif operation == 'd':
  print("A divisão entre os 2 números é: ", num1 / num2)

else:
  print ("Você não digitou uma condicional válida")
