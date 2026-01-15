"""
CSV Extraction Module
Reads customer data from CSV files
"""

import pandas as pd
from pathlib import Path


def extract_customers(file_path='data/customers.csv'):
    """
    Extract customer data from CSV file
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Customer data
    """
    print("\n" + "="*60)
    print("[EXTRACT - CSV]")
    print("="*60)
    
    print(f"📄 Reading customers from {file_path}")
    
    try:
        # Check file exists
        if not Path(file_path).exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        
        # Read CSV
        df = pd.read_csv(file_path)
        
        # Convert date column
        df['signup_date'] = pd.to_datetime(df['signup_date'])
        
        print(f"✅ Extracted {len(df)} customers")
        print(f"   Columns: {', '.join(df.columns)}")
        
        return df
        
    except Exception as e:
        print(f"❌ CSV extraction failed: {e}")
        raise


# Test function
if __name__ == '__main__':
    print("🧪 Testing CSV extraction...")
    customers = extract_customers()
    print("\n📊 Sample data:")
    print(customers.head())
    print(f"\n✅ Extraction test passed: {len(customers)} records")