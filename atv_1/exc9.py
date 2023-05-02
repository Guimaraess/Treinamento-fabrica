string = input("Digite uma string: ")
letras = 0

for caractere in string:
    if caractere.isalpha():
        letras += 1

print("Número de letras na string: ", letras)
