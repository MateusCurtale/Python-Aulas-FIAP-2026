# Estruturas condicionais

# Estrutura condicional simples
nota_final = 4

if nota_final < 4:
    print("Reprovado")

# Estrutura condicional composta
nota_final = 4

if nota_final < 4:
    print("Reprovado")
else:
    print("Aprovado")

# Estrutura condicional encadeada
nota_final = 3

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")


# Estrutura condicional encadeada - elif
if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovada")