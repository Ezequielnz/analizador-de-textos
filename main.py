#Desafío 2: analizador de textos

#variables
text = input("ingrese una cadena de texto: ")
letras = input("ingrese tres letras a elección: ")[:3]
lista_letras = []

text_lower = text.lower()

#procesos

#convertir a minúscula
letras_lower = letras.lower()

#agrega las letras sin caracteres especiales
for letra in letras_lower:
    if letra.isalpha():
        lista_letras.append(letra)

#contar cuantas veces aparecen las letras en el texto
for letra in lista_letras:
    contador = text_lower.count(letra)
    print(f"\nLa letra '{letra}' aparece {contador} veces en la cadena.\n")

#lista de palabras
text_list = text_lower.split()
print(f"el texto ingresado tiene la cantidad de: {len(text_list)} palabras.\n")

#la primera y última letra del texto
print(f"la primera letra del texto es: {text[0]}, y la última: {text[-1]}\n")

#mostrar el text en orden inverso
text_inverso = ''.join(reversed(text))
print(text_inverso)

#verificar si aparece la palabra python
if text_lower.find("python"):
    print("\nsi se encuentra la palabra python")
else:
    print("\nno se encuentra la palabra python")
