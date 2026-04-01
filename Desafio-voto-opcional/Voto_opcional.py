
idade = 0
while idade < 1: # Impede o usuário de digitar um valor nulo.
    idade = int(input("Digite sua idade: "))

if 16 <= idade and idade < 18 or idade > 70:
    print("Seu voto é opcional!")
elif idade < 16:
    print("Você não pode votar")
else:
    print("Seu voto é obrigatório!")

