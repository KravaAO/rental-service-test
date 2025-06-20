# Rental Service API

## Apartments

Base URL: `/api/v1/apartments/`

- **GET /api/v1/apartments/** — список квартир (фільтри: search, ordering, availability)
- **POST /api/v1/apartments/** — створити нову квартиру (авторизація)
- **GET /api/v1/apartments/{slug}/** — деталі квартири
- **PUT/PATCH /api/v1/apartments/{slug}/** — редагування квартири (тільки власник)
- **DELETE /api/v1/apartments/{slug}/** — видалення квартири (тільки власник)

Фільтри:
- `available=true` — тільки доступні
- `search` — пошук по назві/опису
- `ordering` — сортування: price_max, price_min, rooms, -rooms, created_at, -created_at

---

## Users & Auth

Base URL: `/api/v1/users/`

- **GET /api/v1/users/users/** — список користувачів (тільки для адміністратора)
- **GET /api/v1/users/users/{id}/** — деталі користувача (тільки для адміністратора)

JWT авторизація:
- **POST /api/v1/users/api/token/** — отримати токен (login)
  - body: `{ "email": "user@example.com", "password": "..." }`
- **POST /api/v1/users/api/token/refresh/** — оновити токен
  - body: `{ "refresh": "..." }`


### Приклад запиту на отримання квартир
```
GET /api/v1/apartments/?availability=true&ordering=-price&search=центр
```

### Приклад логіну
```
POST /api/v1/users/api/token/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

---

> Для повного переліку полів дивіться Swagger-документацію `/api/v1/docs/`.
## Factory Boy (seed-скрипти)

- **Створити тестові дані (користувачі та квартири):**

    ```sh
    docker compose exec backend python manage.py seed_apartments --users 30 --apartments 20
    ```

- **Додати лише квартири:**

    ```sh
    docker compose exec backend python manage.py seed_apartments --apartments 20
    ```

- **Додати лише користувачів:**

    ```sh
    docker compose exec backend python manage.py seed_apartments --users 30
    ```

---

## Docker-команди для запуску

- **Запустити всі сервіси:**

    ```sh
    docker compose up --build
    ```

- **Зупинити всі сервіси:**

    ```sh
    docker compose down
    ```

- **Перезапустити з перебілдом:**

    ```sh
    docker compose down -v
    docker compose build --no-cache
    docker compose up
    ```

- **Переглянути логи:**

    ```sh
    docker compose logs -f
    ```
