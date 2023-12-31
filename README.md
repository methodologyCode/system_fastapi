# Система рассмотрения жалоб.

```
- Сделано на основе ролевой модели.
- Доступ к маршруту(функционалу) зависит от роли.

- Регистрация
- Логин(JWT token)

- Получение всех притензий(Админ)
- Получение своих притензий(Аппелянт)
- Получение только тех притензий, которые находятся в статусе ожидания(Проверяющий)

- Создание притензии(Аппелянт, при регистрации по умолчанию)
- Удаление притензии(Админ)

- Одобрение притензии(Проверяющий)
- Отклонение притензии(Проверяющий)

- Получение всех/одного юзера/ов(Админ)
- Сделать конкретного юзера админом(Админ)
- Сделать конкретного юзера проверяющим(Админ)

- Реализована консольная команда регистрирующая администратора.
```

## Запуск приложения
Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:  
```
uvicorn main:app --reload
```

### Документация
```
- http://IP/docs#/
```

### Стек
```
Python 3.8, FastApi, PostgreSQL, Sqlalchemy, Alembic.
```
