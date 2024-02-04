![example workflow](https://github.com/Michelin90/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# YaCut

## Описание:
Сервис укорачивания ссылок и API к нему.

Ключевые возможности сервиса:

- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой
## Язык и инструменты:
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-blue?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-blue?style=for-the-badge&logo=SQLAlchemy)](https://www.sqlalchemy.org/)

## Автор:
Михаил [Michelin90](https://github.com/Michelin90) Хохлов

## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Michelin90/yacut.git
```
```
cd yacut
```
### Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```
* Если у вас windows

    ```
    source venv/scripts/activate
    ```
### Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
flask db upgrade
```
### Запустить приложение:
```
flask run
```
Приложение будет доступно по адресу: http://127.0.0.1:5000/

## Примеры запросов к API:
В [онлайн-редакторе Swagger](https://editor.swagger.io/) откройте файл **openapi.yml** для ознакомления c примерами запросов к API.
