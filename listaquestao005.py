#Questão 5 da lista de exercícios.
salario = int(input('Digite o salário: '))
aumento = int(input('Digite a porcentagem do aumento: '))

salaumento = (aumento / 100 *salario) + salario

print('aumento: {:.2f}'.format(aumento /100 * salario))
print('salário novo: {:.2f}'.format(salaumento))