# Book-Store-API
API-сервис для книжного магазина
## Требования
```virtualenv==15.0.1```

```python3```

```curl v7.47.0```

## Порядок запуска
1. Настроить интерпретатор
2. Установить зависимости
3. Запустить main.py

## End-point'ы и примеры запросов

## Book

### 0.0.0.0:5000/Book/AddBook

method = POST

Вносит книгу в бд, возвращая сохраненные данные

Пример запроса:

```curl -H "Content-Type: application/json" -X POST -d '{"ISBN_code":<ISBN_code>, "name":<name>, "category":<category>, "price":<price>}' 0.0.0.0:5000/Book/AddBook```

### 0.0.0.0:5000/Book/GetBook

method = GET

Возвращает книгу по ее ISBN-коду

Пример запроса:

```curl -H "Content-Type: application/json" -X GET -d '{"ISBN_code":<ISBN_code>}' 0.0.0.0:5000/Book/GetBook```

### 0.0.0.0:5000/Book/DeleteBook

method = DELETE

Удаляет книгу из бд по ее ISBN-коду

Пример запроса:

```curl -H "Content-Type: application/json" -X DELETE -d '{"ISBN_code":<ISBN_code>}' 0.0.0.0:5000/Book/DeleteBook```

### 0.0.0.0:5000/Book/GetAllBooks

method = GET

Возвращает все книги в соответствии со входными параметрами, каждый из параметров можно опустить

Пример запроса:

```curl -H "Content-Type: application/json" -X GET -d '{"category":<category>, "price_min":<price_min>, "price_max":<price_max>}' 0.0.0.0:5000/Book/GetAllBooks```

#### Использованные переменные и ограничения

ISBN_code - может содержать только цифры и дефисы, длина - 13 символов

category - может принимать одно из трех значений: 'art', 'business', 'science-popular'

price - не может принимать отрицательные значения

## User

### 0.0.0.0:5000/User/AddUser

method = POST

Вносит пользователя в бд, возвращая сохраненные данные

Пример запроса:

```curl -H "Content-Type: application/json" -X POST -d '{"name":<name>, "mail":<mail>, "phone_number":<phone_number>}' 0.0.0.0:5000/User/AddUser```

### 0.0.0.0:5000/User/GetUser

method = GET

Возвращает пользователя по его почтовому адресу

Пример запроса:

```curl -H "Content-Type: application/json" -X GET -d '{"mail":<mail>}' 0.0.0.0:5000/User/GetUser```

### 0.0.0.0:5000/User/DeleteUser

method = DELETE

Удаляет пользователя из бд по его почтовому адресу

Пример запроса:

```curl -H "Content-Type: application/json" -X DELETE -d '{"mail":<mail>}' 0.0.0.0:5000/User/DeleteUser```

### Использованные переменные и ограничения
mail - должен содержать почтовый адрес

phone_number - должен содержать только цифры, длина - 11 символов 

## Transaction

### 0.0.0.0:5000/Transaction/Create

method = POST

Создает экземпляр транзакции по входным данным

Пример запроса:

```curl -H "Content-Type: application/json" -X POST -d '{"mail":<mail>, "Books_ISBNs":[<ISBN1>,<ISBN2>,..,<ISBNn>]}' 0.0.0.0:5000/Transaction/Create```

### 0.0.0.0:5000/Transaction/Get

method = GET

Возвращает транзакцию по ее id

Пример запроса:

```curl -H "Content-Type: application/json" -X GET -d '{"id":<id>}' 0.0.0.0:5000/Transaction/Get```

### 0.0.0.0:5000/Transaction/Delete

method = DELETE

Удаляет транзакцию по ее id

Пример запроса:

```curl -H "Content-Type: application/json" -X DELETE -d '{"id":<id>}' 0.0.0.0:5000/Transaction/Delete```
