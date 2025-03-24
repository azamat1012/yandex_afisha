# Yandex Afisha

Этот скрипт позволяет добавлять любимые места и просматривать их на карте.

---

## <h2 style="text-align:center">Демо-версия</h2>

Демо-версия сайта доступна по [ссылке](https://aza004mat.pythonanywhere.com/)

---

## <h2 style="text-align:center">Окружение</h2>

### Требования

Для работы требуется установленная версия Python 3.11.5. Рекомендуется создать виртуальное окружение, чтобы не засорять основное пространство.

- Установите следующие зависимости в ваше окружение:

1. Django==5.1.7
2. django-admin-sortable2==2.2.4
3. django-tinymce==4.1.0
4. pillow==11.1.0
5. python-environ==0.4.54

Или выполните команду в терминале:

```bash
pip install -r requirements.txt
```

В файле .env укажите кастомные переменные окружения:

```bash
SECRET_KEY="Ваш_секретный_ключ"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB=sqlite
```

Генерировать безопасный SECRET_KEY можно с помощью Python:

```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
```

Этот код создаст строку вроде p@9v#k&x)mzq-5j!n2r+t8u$y_l0e\*hw

Для чего нужен:

- SECRET_KEY - это секретный ключ, который используется Django для поддержки безопасности сайта.
- DEBUG - Программа-отладчик, которую используют для проверки и отладки выполняемых файлов.
- ALLOWED_HOSTS - это адрес, где будет показываться Ваш сайт
- DB - это база данных откуда скрипт берет даннные (Данная переменная необязательная)

Выполнение миграций

```bash
python manage.py migrate
```

Запуск

```bash
python manage.py runserver
```

Сайт будет доступен по адресу: <strong>http://127.0.0.1:8000/</strong>

<h2 style="text-align:center">Примечания</h2>
Если вы хотите зайти в админ-панель, выполните следующие шаги:
<br/>
<br/>
<br/>

1. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

Введите имя пользователя, email и пароль.
<br/>
<br/> 2. Перезапустите сервер:

```bash
python manage.py runserver
```

<br/>
<br/>
3. Перейдите в админ-панель по адресу:
<strong> http://127.0.0.1:8000/admin/</strong>

В админ-панели вы можете добавлять новые места и видеть изменения на главной странице.

<h2 style="text-align:center">Загрузка мест</h2>
Для загрузки данных о местах используйте команду:

```bash
python manage.py load_place "URL_к_JSON_файлу"
```

Пример URL:
https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Лопатинский%20рудник.json

<br/>
<br/>

Пример JSON-файла с локацией

```json
{
  "title": "Лопатинский рудник",
  "description_short": "Карьер с бирюзовой водой и песчаными берегами.",
  "description_long": "<p>Лопатинский рудник — это заброшенный фосфоритный карьер в Московской области...</p>",
  "coordinates": {
    "lng": 38.789,
    "lat": 55.123
  },
  "imgs": [
    "https://example.com/images/5daa6346a8294570ddeeaa79e2fbdaf3.jpg",
    "https://example.com/images/d18243f83f4f75109ba18f5f57cc82fa.jpg"
  ]
}
```

<br/>
<br/>
<br/>
<h2 style="text-align:center">Цели проекта</h2>
Код написан для упрощения интерфейса пользователя, чтобы легко просматривать любимые места на карте!
