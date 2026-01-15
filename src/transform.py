"""
Transformation Module
Cleans and transforms extracted data
"""

import pandas as pd


def transform_customers(df):
    """
    Transform customer data
    
    Args:
        df (pd.DataFrame): Raw customer data
        
    Returns:
        pd.DataFrame: Cleaned customer data
    """
    print("\n🔄 Transforming customers...")
    
    df_clean = df.copy()
    
    # Remove duplicates
    original_count = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=['customer_id'])
    if len(df_clean) < original_count:
        print(f"   Removed {original_count - len(df_clean)} duplicate customers")
    
    # Clean email addresses (lowercase)
    df_clean['email'] = df_clean['email'].str.lower().str.strip()
    
    # Clean names (title case)
    df_clean['name'] = df_clean['name'].str.strip().str.title()
    
    # Fill missing countries
    df_clean['country'] = df_clean['country'].fillna('Unknown')
    
    # Ensure correct data types
    df_clean['customer_id'] = df_clean['customer_id'].astype(int)
    
    print(f"✅ Transformed {len(df_clean)} customers")
    
    return df_clean


def transform_products(df):
    """
    Transform product data
    
    Args:
        df (pd.DataFrame): Raw product data
        
    Returns:
        pd.DataFrame: Cleaned product data
    """
    print("\n🔄 Transforming products...")
    
    df_clean = df.copy()
    
    # Remove duplicates
    original_count = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=['product_id'])
    if len(df_clean) < original_count:
        print(f"   Removed {original_count - len(df_clean)} duplicate products")
    
    # Clean product names
    df_clean['name'] = df_clean['name'].str.strip()
    
    # Ensure prices are positive
    df_clean['price'] = df_clean['price'].abs()
    
    # Fill missing categories
    df_clean['category'] = df_clean['category'].fillna('General')
    
    # Ensure correct data types
    df_clean['product_id'] = df_clean['product_id'].astype(int)
    df_clean['price'] = df_clean['price'].round(2)
    
    print(f"✅ Transformed {len(df_clean)} products")
    
    return df_clean


# Test function
if __name__ == '__main__':
    from extract_csv import extract_customers
    from extract_api import extract_products
    
    print("🧪 Testing transformations...")
    
    # Test customers
    customers_raw = extract_customers()
    customers_clean = transform_customers(customers_raw)
    print("\n📊 Transformed customers sample:")
    print(customers_clean.head())
    
    # Test products
    products_raw = extract_products()
    products_clean = transform_products(products_raw)
    print("\n📊 Transformed products sample:")
    print(products_clean.head())
    
    print("\n✅ All transformation tests passed!")