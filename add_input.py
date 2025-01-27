# Grade 1. Этап 1: Задание 3

username =  input("Введите имя пользователя: ")
title = input("Введите название заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (Активная/Неактивная): ")
created_date = input("Введите дату создания заметки (ДД-ММ-ГГГГ): ")
issue_date = input("Введите дедлайн заметки (ДД-ММ-ГГГГ): ")

print(f"Имя пользователя: {username}")
print(f"Заголовок заметки: {title}")
print(f"Описание заметки: {content}")
print(f"Статус заметки: {status}")
print(f"Дата создания заметки: {created_date[0:5]}")
print(f"Дедлайн заметки: {issue_date[0:5]}")