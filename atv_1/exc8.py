frase = input("Digite uma frase: ")
palavra1 = input("Digite a palavra a ser substituída: ")
palavra2 = input("Digite a palavra substituta: ")

nova_frase = frase.replace(palavra1, palavra2, 1)

print("Frase original: ", frase)
print("Nova frase: ", nova_frase)
