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
#### 📅 Week 1 — Foundation and Structure
**🎯 Goal:** Project skeleton, authentication, database

**Backend:**
- [ ] FastAPI + Docker
- [ ] SQLAlchemy + Alembic
- [X] Auth: JWT (registration, login, /me)
- [ ] Models: User, Product, Category, CartItem
- [X] Endpoints:
    - [X] POST /register
    - [X] POST /login
    - [X] GET /me
    - [X] GET /products/
    - [X] GET /products/{id}

**Frontend:**
- [] React scaffolding (Vite or Create React App)
- [ ] React Router (routes: /, /product/:id, /login, /register)
- [ ] Axios
- [ ] Display product list (unstyled for now)
- [ ] Components: ProductCard, ProductPage, Header

**DevOps:**
- [ ] Docker Compose: frontend, backend, db
- [ ] SQLite or PostgreSQL (depending on experience)

---

#### 📅 Week 2 — Cart and Logic
**🎯 Goal:** User, cart, adding products

**Backend:**
- [ ] Cart model: CartItem (user_id, product_id, quantity)
- [ ] Endpoints:
    - [ ] POST /cart/add
    - [ ] GET /cart/
    - [ ] DELETE /cart/{item_id}
- [ ] Basic rules: do not add the same product twice, increase quantity instead

**Frontend:**
- [ ] Cart with local or global state (Context or Redux)
- [ ] Cart page
- [ ] Authentication integration: storing JWT
- [ ] Display user profile (GET /me)
- [ ] Simple design (Tailwind or plain CSS)

---

#### 📅 Week 3 — Polishing, Admin Panel, Extras
**🎯 Goal:** Make the MVP beautiful and stable

**Backend:**
- [ ] Admin panel: POST /products/ for adding products
- [ ] Product categories: GET /categories/
- [ ] Product filtering by categories (query parameter)
- [ ] Validations, error handling, Swagger documentation

**Frontend:**
- [ ] Product filtering by categories
- [ ] Forms for registration, login, adding products
- [ ] Design improvements, responsiveness
- [ ] Error handling (e.g., invalid login)

