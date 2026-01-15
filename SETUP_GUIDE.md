# 🛠️ Setup Guide

Complete setup instructions for the Multi-Source Integration Pipeline.

## Prerequisites

- PostgreSQL 13+
- Python 3.8+
- Internet connection (for API)

## Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-source-integration.git
cd multi-source-integration
```

## Step 2: Create Database
```bash
createdb integration_db
```

## Step 3: Create Tables
```bash
psql -d integration_db -f sql/schema.sql
```

**Expected output:**
```
DROP TABLE
DROP TABLE
CREATE TABLE
CREATE INDEX
...
```

## Step 4: Install Python Packages
```bash
pip install -r requirements.txt
```

## Step 5: Configure Environment
```bash
cp .env.example .env
```

Edit `.env` with your database credentials.

## Step 6: Test Connection
```bash
python -c "import psycopg2; from config import config; conn = psycopg2.connect(config.db_connection_string); print('✅ Connected')"
```

## Step 7: Run Pipeline
```bash
python main.py
```

## Step 8: Verify Data
```bash
psql -d integration_db -f sql/queries.sql
```

## Troubleshooting

**"Cannot connect to database"**
- Check PostgreSQL is running: `pg_isready`
- Verify credentials in `.env`

**"File not found"**
- Make sure you're in the project root
- Check `data/customers.csv` exists

**"API request failed"**
- Check internet connection
- API might be down (it's a demo API)

## Total Setup Time

~10 minutes

---

**You're ready to go!** 🚀