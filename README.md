<div align="center">

```
███████╗███╗   ███╗██████╗ ██╗      ██████╗ ██╗   ██╗███████╗███████╗
██╔════╝████╗ ████║██╔══██╗██║     ██╔═══██╗╚██╗ ██╔╝██╔════╝██╔════╝
█████╗  ██╔████╔██║██████╔╝██║     ██║   ██║ ╚████╔╝ █████╗  █████╗  
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══╝  
███████╗██║ ╚═╝ ██║██║     ███████╗╚██████╔╝   ██║   ███████╗███████╗
╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
                        R E S T   A P I
```

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/REST-API-FF6B6B?style=for-the-badge&logo=postman&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Active-00D084?style=for-the-badge"/>

<br/>

> 🚀 **A blazing-fast, minimal REST API for managing your workforce data — built with Flask.**

</div>

---

## 🌈 What Is This?

The **Employee Management REST API** is a clean, no-frills backend service for performing full **CRUD operations** on employee records. Perfect as a starter backend, learning project, or microservice foundation.

```
POST   ──►  Add a new hire
GET    ──►  List the whole team
PUT    ──►  Update someone's details
DELETE ──►  Offboard gracefully
```

---

## ✨ Features at a Glance

| 🟢 Feature | 📋 Description |
|---|---|
| 🔍 **View All Employees** | Fetch the entire employee list in one call |
| ➕ **Add Employee** | Onboard new staff with name, role & salary |
| ✏️ **Update Employee** | Modify any field of an existing record |
| 🗑️ **Delete Employee** | Remove a record cleanly by index |
| ⚡ **Zero DB Setup** | In-memory storage — runs instantly |
| 🛡️ **Input Validation** | Returns clear errors for bad requests |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | 🐍 Python 3 |
| **Framework** | 🌐 Flask |
| **Storage** | 🧠 In-Memory (List) |
| **Data Format** | 📦 JSON |

</div>

---

## ⚡ Quick Start

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/employee-api.git
cd employee-api
```

### 2️⃣ Install dependencies
```bash
pip install flask
```

### 3️⃣ Fire it up 🔥
```bash
python app.py
```

```
 * Running on http://127.0.0.1:5000
 * Debug mode: ON
```

---

## 📡 API Reference

### 🔵 `GET /employees`
> Retrieve all employee records.

```bash
curl http://127.0.0.1:5000/employees
```

**Response `200 OK`**
```json
[
  { "name": "Alice", "role": "Engineer", "salary": 90000 },
  { "name": "Bob",   "role": "Designer", "salary": 75000 }
]
```

---

### 🟢 `POST /employees`
> Add a new employee to the system.

```bash
curl -X POST http://127.0.0.1:5000/employees \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "role": "Engineer", "salary": 90000}'
```

| Field | Type | Required | Default |
|---|---|---|---|
| `name` | string | ✅ Yes | — |
| `role` | string | ✅ Yes | — |
| `salary` | number | ❌ No | `0` |

**Response `201 Created`**
```json
{
  "message": "Employee added",
  "employee": { "name": "Alice", "role": "Engineer", "salary": 90000 }
}
```

---

### 🟡 `PUT /employees/<index>`
> Update an existing employee by list index.

```bash
curl -X PUT http://127.0.0.1:5000/employees/0 \
  -H "Content-Type: application/json" \
  -d '{"salary": 100000}'
```

**Response `200 OK`**
```json
{
  "message": "Employee updated",
  "employee": { "name": "Alice", "role": "Engineer", "salary": 100000 }
}
```

---

### 🔴 `DELETE /employees/<index>`
> Remove an employee by list index.

```bash
curl -X DELETE http://127.0.0.1:5000/employees/0
```

**Response `200 OK`**
```json
{
  "message": "Employee deleted",
  "employee": { "name": "Alice", "role": "Engineer", "salary": 100000 }
}
```

---

## 🗂️ Project Structure

```
📦 employee-api/
├── 📄 app.py          ← Main application & all routes
└── 📄 README.md       ← You are here!
```

---

## ⚠️ Important Notes

> 💾 **Data is stored in-memory.** All records are lost when the server restarts. For persistence, consider integrating SQLite or PostgreSQL.

> 🔢 **Index-based routing.** Employee `<index>` is **zero-based** — the first employee is at index `0`.

> 🔒 **No authentication.** This is a development-ready API. Add JWT or API key auth before deploying to production.

---

## 🗺️ Roadmap

- [ ] 🗃️ Add database persistence (SQLite / PostgreSQL)
- [ ] 🔐 Authentication & Authorization (JWT)
- [ ] 🆔 Switch from index-based to UUID-based routing
- [ ] 📖 Swagger / OpenAPI documentation
- [ ] 🧪 Unit & integration tests
- [ ] 🐳 Dockerize the app

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the project 🍴
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request 🎉

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and ☕

**⭐ Star this repo if you found it helpful!**

</div>
