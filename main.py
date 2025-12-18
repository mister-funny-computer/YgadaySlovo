print("Давай поиграем. Я загадал слово, тебе нужно его отгадать по буквам")

secret_word = "deltarune"
attempts = 5
letters = []

while attempts > 0:
    letter = input("Введите букву: ")
    print(f"Твоя буква {letter}")
    letters.append(letter)
    print(letters)
