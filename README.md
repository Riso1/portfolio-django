# Portfolio Django

Персональный сайт-портфолио, разработанный на Django.

Проект создан для демонстрации навыков backend и fullstack-разработки, а также для публикации проектов, сертификатов, опыта и контактной информации.

## Технологии

- Python 3.13
- Django 6
- SQLite
- Bootstrap 5
- HTML5 / CSS3
- Font Awesome
- python-dotenv

## Реализованный функционал

### Контент через админ-панель

- Управление разделами сайта
- Управление технологиями
- Управление проектами
- Управление сертификатами
- Управление контактами
- Управление опытом и образованием

### Портфолио

- Отдельные страницы проектов
- Изображения проектов
- GitHub и Demo ссылки
- SEO-настройки

### Дополнительно

- Open Graph для Telegram и социальных сетей
- Favicon из админки
- Sitemap.xml
- Robots.txt
- Кастомная страница 404
- Адаптивный интерфейс

## Установка

```bash
git clone <repository_url>
cd portfolio-django
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Настройка окружения

Создать файл `.env`:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Миграции

```bash
python manage.py migrate
```

## Создание администратора

```bash
python manage.py createsuperuser
```

## Запуск проекта

```bash
python manage.py runserver
```

## Подготовка статических файлов

```bash
python manage.py collectstatic
```

## Автор

Александр Котелевский

Python Developer | Django Developer

GitHub: Riso1