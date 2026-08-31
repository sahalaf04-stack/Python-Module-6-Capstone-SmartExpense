# 💰 SmartExpense – Python Capstone Project

A portfolio-ready **Expense Tracker REST API** built using Python and FastAPI. The application allows users to manage expenses, store data in SQLite, perform CRUD operations, validate input, and view spending summaries.

---

## 📌 Project Overview

**SmartExpense** is a Python-based expense tracking application developed as the capstone project for **Module 6 – Python Capstone Project**.

The application provides a REST API for managing personal expenses. It demonstrates real-world Python application development concepts including API development, database integration, authentication, validation, exception handling, logging, and automated testing.

### Main Objectives

* Build a complete Python application
* Develop REST API endpoints
* Implement CRUD operations
* Integrate SQLite database
* Add authentication
* Validate user input
* Implement exception handling
* Add application logging
* Test API endpoints
* Create complete project documentation

---

# ✨ Features

### 💸 Expense Management

* Add new expenses
* View all expenses
* View a specific expense
* Update expenses
* Delete expenses

### 📊 Expense Summary

* Calculate total spending
* Count total expenses
* Display spending by category

### 🔐 Authentication

* API-key authentication
* Protected create, update and delete operations

### ✅ Data Validation

* Expense title validation
* Amount validation
* Category validation
* Description validation

### 🛡️ Error Handling

The application handles:

* Expense not found
* Invalid API key
* Invalid request data
* Invalid expense amounts

### 📝 Logging

Application events such as creating, updating and deleting expenses are recorded using Python logging.

---

# 🏗️ Architecture

The application follows a layered architecture.

```text
                 ┌───────────────────┐
                 │      Client       │
                 │ Web / API Client  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │     FastAPI       │
                 │   REST Endpoints  │
                 └─────────┬─────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌───────────┐ ┌───────────┐
        │ Pydantic │ │    Auth   │ │ Exception │
        │Validation│ │ API Key   │ │ Handling  │
        └────┬─────┘ └───────────┘ └───────────┘
             │
             ▼
        ┌──────────────┐
        │  SQLAlchemy  │
        │     ORM      │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │    SQLite    │
        │   Database   │
        └──────────────┘
```

---

# 🛠️ Technologies

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Application development |
| FastAPI      | REST API framework      |
| SQLite       | Database                |
| SQLAlchemy   | Database ORM            |
| Pydantic     | Data validation         |
| Pytest       | Automated testing       |
| Uvicorn      | ASGI server             |
| HTML         | Frontend structure      |
| CSS          | Frontend styling        |
| JavaScript   | Frontend functionality  |
| Git & GitHub | Version control         |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/sahalaf04-stack/Python-Module-6-Capstone-SmartExpense.git
```

Navigate into the project:

```bash
cd Python-Module-6-Capstone-SmartExpense
```

---

## 2. Install dependencies

Navigate to the backend:

```bash
cd backend
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 3. Start the FastAPI server

Run:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 4. Open API Documentation

FastAPI provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 🔗 API Endpoints

| Method | Endpoint         | Description         | Authentication |
| ------ | ---------------- | ------------------- | -------------- |
| GET    | `/`              | API welcome message | ❌              |
| POST   | `/expenses`      | Create expense      | ✅              |
| GET    | `/expenses`      | Get all expenses    | ❌              |
| GET    | `/expenses/{id}` | Get one expense     | ❌              |
| PUT    | `/expenses/{id}` | Update expense      | ✅              |
| DELETE | `/expenses/{id}` | Delete expense      | ✅              |
| GET    | `/summary`       | Get expense summary | ❌              |

---

# 🗄️ Database Schema

The application uses a SQLite database named:

```text
expense_tracker.db
```

The main table is:

### `expenses`

| Column      | Type     | Description          |
| ----------- | -------- | -------------------- |
| id          | Integer  | Primary key          |
| title       | String   | Expense title        |
| amount      | Float    | Expense amount       |
| category    | String   | Expense category     |
| description | String   | Optional description |
| created_at  | DateTime | Creation timestamp   |

### Example Record

```json
{
    "id": 1,
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "description": "Lunch expense"
}
```

---

# 🔐 Authentication

Protected API endpoints use API-key authentication.

The API key must be sent through the following HTTP header:

```text
X-API-Key
```

Example:

```text
X-API-Key: smartexpense-key
```

Protected operations include:

```text
POST /expenses
PUT /expenses/{id}
DELETE /expenses/{id}
```

> The API key used in this project is intended for local development and demonstration purposes.

---

# 🧪 Testing

Automated API tests are implemented using **Pytest**.

Navigate to the backend:

```bash
cd backend
```

Run:

```bash
pytest
```

The tests verify important application functionality such as:

* API availability
* Expense retrieval
* Expense summary
* Expense creation
* API responses

---

# 📸 Screenshots

Add screenshots of the application here after completing the project.

Recommended screenshots:

### 1. SmartExpense Dashboard

```text
Add your dashboard screenshot here.
```

### 2. Swagger API Documentation

```text
Add your Swagger screenshot here.
```

### 3. Expense Creation

```text
Add your POST /expenses screenshot here.
```

### 4. Expense Summary

```text
Add your expense summary screenshot here.
```

### 5. GitHub Repository

```text
Add your GitHub repository screenshot here.
```

---

# 🚀 Deployment

The application can be deployed using cloud hosting platforms that support Python applications.

### Backend

The FastAPI backend can be deployed as a Python web service.

Example start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Frontend

The frontend can be deployed using a static hosting platform.

After deployment, update the frontend API URL:

```javascript
const API_URL = "YOUR_DEPLOYED_API_URL";
```

The deployed application URL should be added to this README once available.

### Live Website

```text
Live Website: [Add your deployed website link here]
```

---

# 🔮 Future Improvements

The following features can be added in future versions:

* User registration and login
* JWT authentication
* Password hashing
* User-specific expenses
* Monthly expense reports
* Expense charts and graphs
* Budget management
* CSV export
* PDF report generation
* Email notifications
* Dark mode
* Mobile-responsive dashboard
* Cloud database integration
* Advanced expense filtering
* AI-based spending insights

---

# 📁 Project Structure

```text
Python-Module-6-Capstone-SmartExpense/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── logger.py
│   ├── exceptions.py
│   ├── requirements.txt
│   │
│   └── tests/
│       └── test_api.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

---

# 🎓 Learning Outcomes

Through this capstone project, I gained practical experience in:

* Python application development
* FastAPI
* REST API development
* SQLite database integration
* SQLAlchemy ORM
* CRUD operations
* Pydantic validation
* API authentication
* Exception handling
* Logging
* Automated API testing
* Git and GitHub
* Application deployment
* Project documentation

---

# 👩‍💻 Author

**Sahala Fathima P A**

Artificial Intelligence & Data Science Student

Python Developer | AI/ML Enthusiast | Full-Stack Developer

---

## ⭐ Project

**SmartExpense – Python Capstone Project**

Built as part of **Module 6 – Python Capstone Project**.
