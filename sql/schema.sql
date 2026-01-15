-- =====================================================
-- Multi-Source Integration Database Schema
-- Simple normalized schema for integrated data
-- =====================================================

-- Drop existing tables
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS products CASCADE;

-- =====================================================
-- CUSTOMERS TABLE (from CSV source)
-- =====================================================

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    signup_date DATE,
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_country ON customers(country);

COMMENT ON TABLE customers IS 'Customer master data from CSV files';

-- =====================================================
-- PRODUCTS TABLE (from API source)
-- =====================================================

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category);

COMMENT ON TABLE products IS 'Product catalog from REST API';

-- =====================================================
-- Verification
-- =====================================================

SELECT 
    'customers' as table_name,
    COUNT(*) as row_count
FROM customers
UNION ALL
SELECT 
    'products',
    COUNT(*)
FROM products;