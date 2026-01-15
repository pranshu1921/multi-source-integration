"""
Load Module
Loads data into PostgreSQL database
"""

import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from config import config


class DataLoader:
    """Handles loading data to PostgreSQL"""
    
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Connect to database"""
        try:
            self.conn = psycopg2.connect(config.db_connection_string)
            self.cursor = self.conn.cursor()
            print("✅ Connected to database")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            raise
    
    def disconnect(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("🔌 Disconnected from database")
    
    def load_customers(self, df):
        """
        Load customers to database
        
        Args:
            df (pd.DataFrame): Customer data
        """
        print(f"\n📥 Loading {len(df)} customers to database...")
        
        # Prepare data
        data = [
            (
                int(row['customer_id']),
                row['name'],
                row['email'],
                row['signup_date'],
                row['country']
            )
            for _, row in df.iterrows()
        ]
        
        # Insert with upsert (ON CONFLICT)
        query = """
            INSERT INTO customers (customer_id, name, email, signup_date, country)
            VALUES %s
            ON CONFLICT (customer_id) 
            DO UPDATE SET 
                name = EXCLUDED.name,
                email = EXCLUDED.email,
                signup_date = EXCLUDED.signup_date,
                country = EXCLUDED.country
        """
        
        try:
            execute_values(self.cursor, query, data)
            self.conn.commit()
            print(f"✅ Loaded {len(data)} customers")
        except Exception as e:
            self.conn.rollback()
            print(f"❌ Failed to load customers: {e}")
            raise
    
    def load_products(self, df):
        """
        Load products to database
        
        Args:
            df (pd.DataFrame): Product data
        """
        print(f"\n📥 Loading {len(df)} products to database...")
        
        # Prepare data
        data = [
            (
                int(row['product_id']),
                row['name'],
                float(row['price']),
                row['category']
            )
            for _, row in df.iterrows()
        ]
        
        # Insert with upsert
        query = """
            INSERT INTO products (product_id, name, price, category)
            VALUES %s
            ON CONFLICT (product_id)
            DO UPDATE SET
                name = EXCLUDED.name,
                price = EXCLUDED.price,
                category = EXCLUDED.category
        """
        
        try:
            execute_values(self.cursor, query, data)
            self.conn.commit()
            print(f"✅ Loaded {len(data)} products")
        except Exception as e:
            self.conn.rollback()
            print(f"❌ Failed to load products: {e}")
            raise
    
    def get_stats(self):
        """Get database statistics"""
        print("\n📊 Database Statistics:")
        
        tables = ['customers', 'products']
        
        for table in tables:
            query = f"SELECT COUNT(*) FROM {table}"
            self.cursor.execute(query)
            count = self.cursor.fetchone()[0]
            print(f"   {table}: {count:,} rows")


# Test function
if __name__ == '__main__':
    from extract_csv import extract_customers
    from extract_api import extract_products
    from transform import transform_customers, transform_products
    from validate import validate_customers, validate_products
    
    print("🧪 Testing load module...")
    
    # Extract
    customers_raw = extract_customers()
    products_raw = extract_products()
    
    # Transform
    customers_clean = transform_customers(customers_raw)
    products_clean = transform_products(products_raw)
    
    # Validate
    if not validate_customers(customers_clean):
        raise ValueError("Customer validation failed")
    if not validate_products(products_clean):
        raise ValueError("Product validation failed")
    
    # Load
    loader = DataLoader()
    try:
        loader.connect()
        loader.load_customers(customers_clean)
        loader.load_products(products_clean)
        loader.get_stats()
    finally:
        loader.disconnect()
    
    print("\n✅ Load test complete!")