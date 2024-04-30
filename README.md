# flexible_onboarding
Flexible onboarding - приложение для гибкого процесса онбординга.

<details>
<summary>
  <strong>
    Как оформлять ветки и коммиты
  </strong>
</summary>

Пример ветки `last_name/name_task`

- **last_name** (фамилия разработчика)
- **name_task** (название задачи)

Пример коммита `refactor: renaming a variable`

- **feat:** (новая функционал кода, БЕЗ учёта функционала для сборок)
- **devops:** (функционал для сборки, - добавление, удаление и исправление)
- **fix:** (исправление ошибок функционального кода)
- **docs:** (изменения в документации)
- **style:** (форматирование, отсутствующие точки с запятой и т.п., без изменения производственного кода)
- **refactor:** (рефакторинг производственного кода, например, переименование переменной)
- **test:** (добавление недостающих тестов, рефакторинг тестов; без изменения производственного кода)
- **chore:** (обновление рутинных задач и т. д.; без изменения производственного кода). 

Оформление основано на https://www.conventionalcommits.org/en/v1.0.0/

</details>

<details>
<summary>
  <strong>
    Стек
  </strong>
</summary>

- **Python 3.11.0**
- **Django 5.0.4**
- **PostgreSQL 13.14**
- **Bootstrap 5**
- **Html**

</details>

<details>
<summary>
  <strong>
    Инструкция по запуску проекта (Ubuntu/Debian)
  </strong>
</summary>

- **postgreSQL** (установите и настройте postgreSQL для своей ОС https://www.postgresql.org/download/)
- **cd `path_project`** (перейти в папку с проектом)
- **sudo nano .env** (создайте .env по образцу .env.example)
- **pip install -r requirements.txt** (установка библиотек и зависимостей)
- **python manage.py migrate** (примените миграции для базы данных)
- **python manage.py runserver** (запустите проект)

</details>