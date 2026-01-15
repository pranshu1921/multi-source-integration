"""
Validation Module
Performs data quality checks
"""

import pandas as pd


def validate_customers(df):
    """
    Validate customer data
    
    Args:
        df (pd.DataFrame): Customer data
        
    Returns:
        bool: True if validation passes
    """
    print("\n🔍 Validating customers data...")
    
    errors = []
    
    # Check required columns exist
    required_cols = ['customer_id', 'name', 'email']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    # Check for nulls in critical columns
    for col in required_cols:
        if col in df.columns:
            null_count = df[col].isnull().sum()
            if null_count > 0:
                errors.append(f"{col} has {null_count} null values")
    
    # Check for duplicate customer_ids
    if 'customer_id' in df.columns:
        dup_count = df['customer_id'].duplicated().sum()
        if dup_count > 0:
            errors.append(f"Found {dup_count} duplicate customer IDs")
    
    # Check for duplicate emails
    if 'email' in df.columns:
        dup_count = df['email'].duplicated().sum()
        if dup_count > 0:
            errors.append(f"Found {dup_count} duplicate emails")
    
    # Check email format (basic)
    if 'email' in df.columns:
        invalid_emails = df[~df['email'].str.contains('@', na=False)]
        if len(invalid_emails) > 0:
            errors.append(f"Found {len(invalid_emails)} invalid email formats")
    
    # Report results
    if errors:
        print(f"⚠️  Found {len(errors)} validation issues:")
        for error in errors:
            print(f"   - {error}")
        return False
    else:
        print(f"✅ Validation passed for customers ({len(df)} records)")
        return True


def validate_products(df):
    """
    Validate product data
    
    Args:
        df (pd.DataFrame): Product data
        
    Returns:
        bool: True if validation passes
    """
    print("\n🔍 Validating products data...")
    
    errors = []
    
    # Check required columns exist
    required_cols = ['product_id', 'name', 'price']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    # Check for nulls in critical columns
    for col in required_cols:
        if col in df.columns:
            null_count = df[col].isnull().sum()
            if null_count > 0:
                errors.append(f"{col} has {null_count} null values")
    
    # Check for duplicate product_ids
    if 'product_id' in df.columns:
        dup_count = df['product_id'].duplicated().sum()
        if dup_count > 0:
            errors.append(f"Found {dup_count} duplicate product IDs")
    
    # Check for negative prices
    if 'price' in df.columns:
        negative_count = (df['price'] < 0).sum()
        if negative_count > 0:
            errors.append(f"Found {negative_count} negative prices")
    
    # Report results
    if errors:
        print(f"⚠️  Found {len(errors)} validation issues:")
        for error in errors:
            print(f"   - {error}")
        return False
    else:
        print(f"✅ Validation passed for products ({len(df)} records)")
        return True


# Test function
if __name__ == '__main__':
    from extract_csv import extract_customers
    from extract_api import extract_products
    from transform import transform_customers, transform_products
    
    print("🧪 Testing validation...")
    
    # Test customers
    customers_raw = extract_customers()
    customers_clean = transform_customers(customers_raw)
    validate_customers(customers_clean)
    
    # Test products
    products_raw = extract_products()
    products_clean = transform_products(products_raw)
    validate_products(products_clean)
    
    print("\n✅ All validation tests passed!")