import random

words = {
    "colores": ["azul", "amarillo", "verde", "rojo", "rosa"],
    "animales": ["pato", "perro", "gato", "ardilla", "ballena"],
    "comidas": ["ravioles", "arroz", "milanesa", "empanada", "pizza"]
}

print("¡Bienvenido al Ahorcado!")
print("Categorías de palabras:")
for clave in words:
    print(f" - {clave}")

category = input("Elegí una categoría: ").lower()

while category not in words:
    print("Categoría no válida \n")
    category = input("Elegí una categoría: ").lower()

word_list = random.sample(words[category], len(words[category]))
total_points = 0
last_word = word_list[-1]

for word in word_list:
    guessed = []
    attempts = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!\n"
                  f"Tu puntaje: {attempts + 6}\n")
            total_points += attempts + 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
        else:
            print("Entrada no válida \n")
            continue
        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}\n"
              f"Tu puntaje: {attempts}\n")
        
    if word != last_word:
        next_round = input("¿Querés seguir jugando?\n"
                           "Si o No ? ").lower()
        while next_round not in ["si", "no"]: 
            print("Entrada no válida \n")
            next_round = input("¿Querés seguir jugando?\n"
                               "Si o No ? ").lower()
        if next_round == "no":
            break
    print()
print("Juego Finalizado\n"
      f"Puntaje Total: {total_points}")
