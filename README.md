# 🔄 Multi-Source Data Integration Pipeline

A simple ETL pipeline that integrates data from multiple sources into a unified PostgreSQL warehouse.

## What This Does

Extracts data from:
- 📄 **CSV files** - Customer master data
- 🌐 **REST API** - Real-time product catalog

Combines them into a single PostgreSQL database for unified analytics.

## Business Case

Many companies have data scattered across different systems:
- Customer data in CSV exports from CRM
- Product data in external API (supplier catalog)
- Need unified view for analytics

This pipeline solves that by:
1. **Extracting** data from CSV and API
2. **Validating** data quality
3. **Loading** into single warehouse

## Tech Stack

- **Python 3.8+** - ETL scripts
- **PostgreSQL** - Data warehouse
- **REST API** - External data source (JSONPlaceholder API)
- **pandas** - Data processing

## Quick Start
```bash
# 1. Create database
createdb integration_db

# 2. Create tables
psql -d integration_db -f sql/schema.sql

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure
cp .env.example .env
# Edit .env with your database info

# 5. Run pipeline
python main.py
```

## Project Structure
```
multi-source-integration/
├── README.md
├── SETUP_GUIDE.md
├── requirements.txt
├── .env.example
├── main.py
│
├── config.py              # Configuration
│
├── src/
│   ├── extract_csv.py     # CSV extraction
│   ├── extract_api.py     # API extraction
│   ├── transform.py       # Data transformation
│   ├── validate.py        # Data validation
│   └── load.py           # Load to database
│
├── sql/
│   ├── schema.sql        # Database schema
│   └── queries.sql       # Sample queries
│
├── data/
│   └── customers.csv     # Sample customer data
│
└── tests/
    └── test_pipeline.py  # Tests
```

## Data Sources

### Source 1: Customer CSV
Local CSV file with customer information:
- customer_id
- name
- email
- signup_date
- country

### Source 2: Product API
JSONPlaceholder API for products:
- product_id
- title
- price
- category

API: `https://jsonplaceholder.typicode.com/users` (demo API)

## What I Learned

- ✅ Multi-source data integration
- ✅ REST API consumption with Python
- ✅ Data validation techniques
- ✅ ETL pipeline design
- ✅ Error handling
- ✅ PostgreSQL integration

## Running the Pipeline
```bash
# Run full pipeline
python main.py

# Test extraction only
python -c "from src.extract_csv import extract_customers; print(extract_customers())"

# Test API extraction
python -c "from src.extract_api import extract_products; print(extract_products())"
```

## Sample Output
```
============================================================
🚀 MULTI-SOURCE INTEGRATION PIPELINE
============================================================

[1/4] EXTRACT - CSV
📄 Reading customers from data/customers.csv
✅ Extracted 50 customers

[2/4] EXTRACT - API
🌐 Fetching products from API
✅ Extracted 10 products

[3/4] TRANSFORM & VALIDATE
🔍 Validating customers data...
✅ Validation passed
🔍 Validating products data...
✅ Validation passed

[4/4] LOAD
📥 Loading 50 customers to database
✅ Loaded customers
📥 Loading 10 products to database
✅ Loaded products

============================================================
✅ PIPELINE COMPLETED SUCCESSFULLY
============================================================
Duration: 3.2 seconds
```

## Database Schema

Simple normalized schema:

**customers table:**
- customer_id (PK)
- name
- email
- signup_date
- country

**products table:**
- product_id (PK)
- name
- price
- category

## Sample Queries
```sql
-- View all customers
SELECT * FROM customers LIMIT 10;

-- View all products
SELECT * FROM products;

-- Count by country
SELECT country, COUNT(*) 
FROM customers 
GROUP BY country 
ORDER BY COUNT(*) DESC;
```

## Future Enhancements

- [ ] Add more data sources (database, S3)
- [ ] Implement incremental loading
- [ ] Add data quality scoring
- [ ] Create dashboard integration
- [ ] Schedule with cron/Airflow

## Author

**[Your Name]**  
GitHub: [@yourusername](https://github.com/yourusername)  
LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

Built to demonstrate multi-source data integration and API consumption skills.

## License

MIT License - see LICENSE file

---

**Last Updated:** January 2026
```

---

#### File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*.pyc
venv/
env/
.venv

# Environment
.env

# Data files (keep sample)
data/*.csv
!data/customers.csv

# Logs
*.log
logs/

# IDE
.vscode/
.idea/
*.swp
.DS_Store

# Database
*.db
*.sqlite

# Testing
.pytest_cache/
```

---

#### File: `LICENSE`
```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

#### File: `requirements.txt`
```
# Core dependencies
pandas==2.0.3
psycopg2-binary==2.9.9
python-dotenv==1.0.0
requests==2.31.0
```

---

#### File: `.env.example`
```
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=integration_db
DB_USER=postgres
DB_PASSWORD=your_password

# API Configuration (using public demo API)
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=30