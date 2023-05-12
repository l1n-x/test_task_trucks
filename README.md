# [Задание](Task.md)
# Развёртывание и запуск

## Шаг 1. Склонировать репозиторий командой

```bash
git clone git@github.com:l1n-x/test_task_trucks.git
```

## Шаг 2. Установить зависимости

### Шаг 2.1 Вариант с `pip`

- Создаём виртуальное окружение и активируем его
```bash
python3 -m venv venv
source venv/bin/activate
```

- Обновляем пакетный менеджер и устанавливаем зависимости
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Шаг 2.2 Вариант с `poetry`

- Устанавливаем `poetry` (Linux/MacOS/Windows(WSL))
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

- Создаём виртуальное окружение и устанавливаем зависимости
```bash
poetry install
```

- Активируем виртуальное окружение
```bash
poetry shell
```

## Шаг 3. Запустить приложение

Т.к. в проекте сохранен экземпляр базы sqlite с тестовыми данными, достаточно запустить Django-сервер:

```bash
python3 manage.py runserver
```

Для доступа в административную панель используются учётные данные: 
```
Login: admin
Password: admin
```