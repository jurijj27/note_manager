# Grade 1. Этап 1: Задание 5

note = {
    "username" : input("Введите имя пользователя: "),
    "content" : input("Введите описание заметки: "),
    "status" : input("Введите статус заметки (Активная/Неактивная): "),
    "created_date" : input("Введите дату создания заметки (ДД-ММ-ГГГГ): "),
    "issue_date" : input("Введите дедлайн заметки (ДД-ММ-ГГГГ): "),
    "title" : 
  [
      input("Введите 1-й заголовок заметки: "),
      input("Введите 2-й заголовок заметки: "),
      input("Введите 3-й заголовок заметки: ")
  ]
}

print(f"\nИмя пользователя: {note.get('username','такого пользователя нет')}")
print(f"Описание заметки: {note.get('content', 'заметка отсутствует')}")
print(f"Статус заметки: {note.get('status', 'статус отсутствует')}")
print(f"Дата создания заметки: {note.get('created_date', 'дата создания отсутствует')[0:5]}")
print(f"Дедлайн заметки: {note.get('issue_date', 'дедлайна нет')[0:5]}")
print(f"Заголовки заметки: {note.get('title', 'Ошибка')[0]}, {note.get('title', '')[1]}, {note.get('title', '')[2]}")
