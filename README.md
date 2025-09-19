# Sweet Shop Management System

The **Sweet Shop Management System** is a full-stack web application built with **React (frontend)** and **FastAPI + PostgreSQL (backend)**. 
It allows admins to manage sweet inventory and customers to browse and purchase sweets in a smooth, interactive UI.

---

##  Features

###  Admin Panel
- Add new sweets with name, price, and quantity.
- Edit or delete existing sweets.
- Manage real-time inventory.

###  Customer Dashboard
- Browse all available sweets.
- Purchase sweets (button disabled when stock is zero).
- Automatic stock deduction when a purchase is made.

### Authentication
- Login & Register functionality for users.

---

## Tech Stack

- **Frontend**: React.js, CSS  
- **Backend**: FastAPI, Python  
- **Database**: PostgreSQL with SQLAlchemy  
- **Other Tools**: Alembic (migrations), ESLint  

---

## 📂 Project Structure

```sweet-shop/
│
├── backend/             # FastAPI backend
│   ├── main.py          # Entry point
│   ├── models.py        # Database models
│   ├── routes/          # API routes
│   └── ...
│
├── frontend1/           # React frontend
│   ├── src/
│   │   ├── components/  # Shared components
│   │   ├── pages/       # Page-level components
│   │   └── styles/      # CSS files
│   └── package.json
│
└── README.md
```

---

## Installation & Setup

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic pydantic[dotenv]
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend1
npm install
npm start
```

---


### Screenshots
 
- ![Dashboard](./home/smriti/sweet_shop_kata/frontend1/screenshots/Dashboard.png)
- ![Login](./home/smriti/sweet_shop_kata/frontend1/screenshots/Login.png)
- ![Register](./home/smriti/sweet_shop_kata/frontend1/screenshots/Register.png)
- ![POS](./home/smriti/sweet_shop_kata/frontend1/screenshots/POS.png)
- ![Admin](./home/smriti/sweet_shop_kata/frontend1/screenshots/Admin.png)


## Future Enhancements
- User roles (Admin vs Customer login).
- Online payment integration.
- Sweet images gallery.
- Order history & billing.

---

## My AI Usage
For this project, I used AI tools to **speed up development, debug issues, and document the project clearly**. 
Here’s how AI supported me:

###  Tools I Used
- **ChatGPT (OpenAI GPT-5)**: For debugging, generating component templates, and improving project structure. 

###  How I Used Them
- **ChatGPT**: 
  - Helped me design React components (`Dashboard`, `AdminPanel`, `InventoryTable`, etc.). 
  - Fixed common React errors like invalid imports, missing exports, and runtime issues. 
  - Suggested dummy data for sweets and implemented "Purchase" functionality with stock updates. 
  - Generated starter CSS for clean UI.

### 💭 Reflection
Using AI tools:
- **Saved time** by quickly solving repetitive coding issues. 
- **Improved learning** as I understood React/JSX import/export rules while fixing errors. 
- **Boosted productivity** — I could focus more on the bigger design instead of wasting time on small syntax/debugging issues. 
- **Documentation clarity** improved because AI helped me structure this README professionally. 

Without AI, I would have spent **much more time debugging imports, writing boilerplate code, and structuring docs**. AI acted like a **coding partner + mentor** throughout the project.

---

##  Author
**Smriti Kanthak** 
MCA Student | Aspiring Software Developer | SPPU
