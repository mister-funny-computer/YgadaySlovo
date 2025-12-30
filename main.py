import random

print("Давай поиграем. Я загадал слово, тебе нужно его отгадать по буквам")

words = [
    "дом", "кот", "собака", "арбуз", "яблоко", "молоко", "хлеб", "стол",
    "стул", "дверь", "окно", "книга", "письмо", "друзья", "улица", "работа",
    "школа", "учитель", "ученик", "цветок", "дерево", "машина", "дорога",
    "фильм", "музыка", "кофе", "чай", "сахар", "соль", "перец", "блюдо",
    "ресторан", "магазин", "парк", "поездка", "роль", "банан", "рыба",
    "такси", "мать", "отец", "брат", "сестра", "деньги", "праздник", "письменный",
    "игра", "досуг", "время", "улица", "жемчуг", "круг", "сердце"
]


secret_word = random.choice(words)
attempts = 7
letters = []

while attempts > 0:
    victory = True
    print(f"У тебя осталось попыток: {attempts}")
    letter = input("Введите букву: ")
    print(f"Твоя буква {letter}")
    letters.append(letter)
    #print(letters)
    for symbol in secret_word:
        if symbol in letters:
            print(symbol, end = "")
        else:
            print("*", end = "")
            victory = False
    print("")

    if letter not in secret_word:
        print("Такой буквы в слове нет")
        attempts = attempts - 1

    if victory == True:
        print("Ты победил")
        break

if attempts == 0:
    print("ты проиграл")
    print(f"Твоё секретное слово {secret_word}")









