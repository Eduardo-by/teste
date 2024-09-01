a = str(input("Digite sua frase: "))


if a.count('a') or a.count('A') > 1:
    print(f"Tem {a.count('a') + a.count('A')} letras A na sua frase")
else:
    print('Não existe letra a em sua frase')
