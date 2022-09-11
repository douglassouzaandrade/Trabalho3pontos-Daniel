#Questão 3 da lista de exercícios.
nota1 = float(input("Escreva uma nota: "))
nota2 = float(input("Escreva uma segunda Nota: "))
nota3 = float(input("Escreva uma terceira Nota: "))
peso1 = float(input("Escreva o peso da primeira nota: "))
peso2 = float(input("Escreva o peso da segunda nota:"))
peso3 = float(input("Escreva o peso da úlitma nota: "))

primeirasoma = nota1*peso1 + nota2*peso2 + nota3*peso3

segundasoma = peso1+peso2+peso3

divisao = primeirasoma/segundasoma

print('O resultado é: {:.2f}'.format(divisao))