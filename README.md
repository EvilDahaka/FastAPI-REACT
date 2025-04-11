# FastAPI-REACT

## Installation## Overview
This project is a full-stack web application built with FastAPI for the backend and React for the frontend.


### Backend (FastAPI)

1.  Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    ```

3.  Activate the virtual environment:

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5.  Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

### Frontend (React)

1.  Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2.  Install the required packages:

    ```bash
    npm install
    ```

3.  Start the React development server:

    ```bash
    npm run dev
    ```
### How to install libraries
1. Go to the backend folder and run the command:
```bash
pip install <library_name>
```
2. Go to the frontend folder and run the command:
```bash
npm install <library_name>
```
### TO DO
📅 Тиждень 1 — Фундамент і кістяк
🎯 Ціль: каркас проєкту, авторизація, база
Backend:

    FastAPI + Docker

    SQLAlchemy + Alembic

    Auth: JWT (реєстрація, логін, /me)

    Моделі: User, Product, Category, CartItem

    Ендпоінти:

        POST /register, POST /login, GET /me

        GET /products/, GET /products/{id}

Frontend:

    React scaffolding (Vite або Create React App)

    React Router (маршрути: /, /product/:id, /login, /register)

    Axios

    Показ списку товарів (поки що без стилів)

    Компоненти: ProductCard, ProductPage, Header

DevOps:

    Docker Compose: frontend, backend, db

    SQLite або PostgreSQL (залежно від досвіду)

📅 Тиждень 2 — Кошик і логіка
🎯 Ціль: користувач, кошик, додавання товарів
Backend:

    Модель кошика: CartItem (user_id, product_id, quantity)

    Ендпоінти:

        POST /cart/add, GET /cart/, DELETE /cart/{item_id}

    Базові правила: не додавати один товар двічі, а збільшувати кількість

Frontend:

    Кошик з локальним або глобальним стейтом (Context або Redux)

    Сторінка кошика

    Інтеграція авторизації: зберігання JWT

    Відображення профілю користувача (GET /me)

    Простий дизайн (Tailwind або просто CSS)

📅 Тиждень 3 — Шліфування, адмінка, бонуси
🎯 Ціль: зробити MVP красивим і стабільним
Backend:

    Адмінка: POST /products/ для додавання товарів

    Категорії товарів: GET /categories/

    Фільтрація товарів по категоріях (query-параметр)

    Валідації, помилки, Swagger документація

Frontend:

    Фільтр товарів по категоріях

    Форма реєстрації, логіну, додавання товару

    Покращення дизайну, адаптивність

    Обробка помилок (наприклад, неправильний логін)

