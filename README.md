# ETL: CSV to SQL

## 📌 Project Overview
This project implements a simple ETL (Extract, Transform, Load) pipeline:

- **Extract**: Read data from CSV files  
- **Transform**: Clean and preprocess the data  
- **Load**: Insert the data into a SQL database  

The goal of this project is to demonstrate basic **data engineering skills**, including:

- Working with structured data (CSV, SQL)  
- Writing modular Python code  
- Following project structure and best practices  
- Using GitHub for version control  

---

## ⚙️ Tech Stack
- Python 3.10+  
- Pandas  
- SQLite (for demo purposes)  
- SQLAlchemy  

---

## 📂 Project Structure
```
etl-csv-to-sql/
│── src/
│   └── etl/
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       └── main.py
│── data/
│   └── sample.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/etl-csv-to-sql.git
   cd etl-csv-to-sql
   ```

2. Create and activate a virtual environment:
   ```bash
   conda create -n data_eng python=3.10 -y
   conda activate data_eng
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the pipeline:
   ```bash
   python src/etl/main.py
   ```

---

## ✅ Example

**Input CSV** (`data/sample.csv`):
```csv
id,name,age
1,Aziz,19
2,Aidar,20
```

**Output in SQLite**:
```sql
SELECT * FROM users;
```

| id | name  | age |
|----|-------|-----|
| 1  | Aziz  | 19  |
| 2  | Aidar | 20  |

---

## 🛠️ Next Steps
- Add logging  
- Add tests (pytest)  
- Dockerize the project  
