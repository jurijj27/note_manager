# Grade 1. Этап 1: Задание 5

note = [
    input("Введите имя пользователя: "),
    input("Введите описание заметки: "),
    input("Введите статус заметки (Активная/Неактивная): "),
    input("Введите дату создания заметки (ДД-ММ-ГГГГ): "),
    input("Введите дедлайн заметки (ДД-ММ-ГГГГ): "),

    [
        input("Введите 1-й заголовок заметки: "),
        input("Введите 2-й заголовок заметки: "),
        input("Введите 3-й заголовок заметки: ")
    ]
]

print(f"Имя пользователя: {note[0]}")
print(f"Описание заметки: {note[1]}")
print(f"Статус заметки: {note[2]}")
print(f"Дата создания заметки: {note[3][0:5]}")
print(f"Дедлайн заметки: {note[4][0:5]}")
print(f"Заголовки заметки: {note[5][0]}, {note[5][1]}, {note[5][2]}")