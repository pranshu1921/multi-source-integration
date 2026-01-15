-- =====================================================
-- Sample Queries for Integrated Data
-- =====================================================

-- View all customers
SELECT * FROM customers ORDER BY signup_date DESC LIMIT 10;

-- View all products
SELECT * FROM products ORDER BY price DESC;

-- Customer count by country
SELECT 
    country,
    COUNT(*) as customer_count
FROM customers
GROUP BY country
ORDER BY customer_count DESC;

-- Product count by category
SELECT 
    category,
    COUNT(*) as product_count,
    ROUND(AVG(price), 2) as avg_price
FROM products
GROUP BY category
ORDER BY product_count DESC;

-- Summary statistics
SELECT 
    'Total Customers' as metric,
    COUNT(*)::TEXT as value
FROM customers
UNION ALL
SELECT 
    'Total Products',
    COUNT(*)::TEXT
FROM products
UNION ALL
SELECT 
    'Countries',
    COUNT(DISTINCT country)::TEXT
FROM customers
UNION ALL
SELECT 
    'Categories',
    COUNT(DISTINCT category)::TEXT
FROM products;