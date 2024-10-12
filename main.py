print('Это тест Какой ты тип игроков из игры "Terraria". Отвечай на вопросы и узнаешь, к какому типу ты относишься!')
question1 = "Сколько у тебя достижений?"
question2 = "Сколько всего боссов в игре?"
question3 = "Какое оружие в игре считается самым сильным?"
question4 = "Что ты используешь при сражении с боссами?"
question5 = "Сколько биомных сундуков ты открыл?"

print(question1)
print("1. Мало. 2. Половина. 3. Все выполнены")
answer1 = input("Введите ответ цифрой: ")
print(question2)
print("1. 12. 2. 18 3. 28.")
answer2 = input("Введите ответ цифрой: ")
print(question3)
print("1. Зенит. 2. Последняя Призма. 3. Нету.")
answer3 = input("Введите ответ цифрой: ")
print(question4)
print("1. Арену. 2. Зелья с едой. 3. Всё перечисленное")
answer4 = input("Введите ответ цифрой: ")
print(question5)
print("1. 6. 2. 3. 3. Нисколько")
answer5 = input("Введите ответ цифрой: ")
terraria_points = 0
if answer1 == "3":
    terraria_points += 1
if answer2 == "3":
    terraria_points += 1
if answer3 == "1":
    terraria_points += 1
if answer4 == "3":
    terraria_points += 1
if answer5 == "1":
    terraria_points += 1
if terraria_points == 5:
    print('Ты относишся к типу игроков игры "Terraria" всезнающий-профессионал.')
else:
    print('Ты относишся к типу игроков игры "Terraria" хороший игрок.')