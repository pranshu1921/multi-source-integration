"""
API Extraction Module
Fetches product data from REST API
"""

import requests
import pandas as pd
from config import config


def extract_products(api_url=None):
    """
    Extract product data from REST API
    
    Args:
        api_url (str): API endpoint URL
        
    Returns:
        pd.DataFrame: Product data
    """
    print("\n" + "="*60)
    print("[EXTRACT - API]")
    print("="*60)
    
    # Use demo API (JSONPlaceholder)
    if api_url is None:
        api_url = f"{config.API_BASE_URL}/users"
    
    print(f"🌐 Fetching products from API")
    print(f"   URL: {api_url}")
    
    try:
        # Make API request
        response = requests.get(
            api_url,
            timeout=config.API_TIMEOUT
        )
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Transform API fields to match our schema
        # JSONPlaceholder returns 'users', we'll treat them as 'products'
        df_products = pd.DataFrame({
            'product_id': df['id'],
            'name': df['name'],
            'price': (df['id'] * 10 + 20).round(2),  # Mock prices
            'category': df['company'].apply(lambda x: x['name'] if isinstance(x, dict) else 'General')
        })
        
        print(f"✅ Extracted {len(df_products)} products")
        print(f"   Columns: {', '.join(df_products.columns)}")
        
        return df_products
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        raise
    except Exception as e:
        print(f"❌ API extraction failed: {e}")
        raise


# Test function
if __name__ == '__main__':
    print("🧪 Testing API extraction...")
    products = extract_products()
    print("\n📊 Sample data:")
    print(products.head())
    print(f"\n✅ Extraction test passed: {len(products)} records")