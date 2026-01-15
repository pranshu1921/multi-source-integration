"""
Simple tests for pipeline components
Run: python tests/test_pipeline.py
"""

import sys
sys.path.insert(0, '.')

from src.extract_csv import extract_customers
from src.extract_api import extract_products
from src.transform import transform_customers, transform_products
from src.validate import validate_customers, validate_products


def test_csv_extraction():
    """Test CSV extraction"""
    print("\n🧪 Testing CSV extraction...")
    df = extract_customers()
    assert len(df) > 0, "No customers extracted"
    assert 'customer_id' in df.columns, "Missing customer_id column"
    assert 'email' in df.columns, "Missing email column"
    print("✅ CSV extraction test passed")


def test_api_extraction():
    """Test API extraction"""
    print("\n🧪 Testing API extraction...")
    df = extract_products()
    assert len(df) > 0, "No products extracted"
    assert 'product_id' in df.columns, "Missing product_id column"
    assert 'name' in df.columns, "Missing name column"
    print("✅ API extraction test passed")


def test_transformation():
    """Test transformation logic"""
    print("\n🧪 Testing transformations...")
    
    # Customers
    customers_raw = extract_customers()
    customers_clean = transform_customers(customers_raw)
    assert len(customers_clean) > 0, "Transformation removed all customers"
    
    # Products
    products_raw = extract_products()
    products_clean = transform_products(products_raw)
    assert len(products_clean) > 0, "Transformation removed all products"
    
    print("✅ Transformation test passed")


def test_validation():
    """Test validation logic"""
    print("\n🧪 Testing validation...")
    
    # Customers
    customers_raw = extract_customers()
    customers_clean = transform_customers(customers_raw)
    assert validate_customers(customers_clean), "Customer validation failed"
    
    # Products
    products_raw = extract_products()
    products_clean = transform_products(products_raw)
    assert validate_products(products_clean), "Product validation failed"
    
    print("✅ Validation test passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("RUNNING PIPELINE TESTS")
    print("="*60)
    
    try:
        test_csv_extraction()
        test_api_extraction()
        test_transformation()
        test_validation()
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED")
        print("="*60)
        
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ TEST ERROR: {e}")
        return False


if __name__ == '__main__':
    success = run_all_tests()
    
    if not success:
        exit(1)