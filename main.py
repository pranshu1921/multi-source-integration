"""
Main Pipeline Orchestrator
Runs the complete multi-source integration pipeline
"""

from datetime import datetime
from src.extract_csv import extract_customers
from src.extract_api import extract_products
from src.transform import transform_customers, transform_products
from src.validate import validate_customers, validate_products
from src.load import DataLoader


def run_pipeline():
    """Execute the complete ETL pipeline"""
    
    start_time = datetime.now()
    
    print("\n" + "="*60)
    print("🚀 MULTI-SOURCE INTEGRATION PIPELINE")
    print("="*60)
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        # ============================================
        # STEP 1: EXTRACT
        # ============================================
        print("\n" + "="*60)
        print("STEP 1: EXTRACT DATA")
        print("="*60)
        
        # Extract from CSV
        customers_raw = extract_customers()
        
        # Extract from API
        products_raw = extract_products()
        
        # ============================================
        # STEP 2: TRANSFORM
        # ============================================
        print("\n" + "="*60)
        print("STEP 2: TRANSFORM DATA")
        print("="*60)
        
        customers_clean = transform_customers(customers_raw)
        products_clean = transform_products(products_raw)
        
        # ============================================
        # STEP 3: VALIDATE
        # ============================================
        print("\n" + "="*60)
        print("STEP 3: VALIDATE DATA")
        print("="*60)
        
        customers_valid = validate_customers(customers_clean)
        products_valid = validate_products(products_clean)
        
        if not customers_valid or not products_valid:
            raise ValueError("Data validation failed")
        
        # ============================================
        # STEP 4: LOAD
        # ============================================
        print("\n" + "="*60)
        print("STEP 4: LOAD TO DATABASE")
        print("="*60)
        
        loader = DataLoader()
        loader.connect()
        
        try:
            loader.load_customers(customers_clean)
            loader.load_products(products_clean)
            loader.get_stats()
        finally:
            loader.disconnect()
        
        # ============================================
        # SUCCESS
        # ============================================
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print("\n" + "="*60)
        print("✅ PIPELINE COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"Duration: {duration:.2f} seconds")
        print(f"Finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n💡 Next steps:")
        print("   1. Connect to database: psql -d integration_db")
        print("   2. Run queries: psql -d integration_db -f sql/queries.sql")
        print("   3. Explore the data!")
        
        return True
        
    except Exception as e:
        print("\n" + "="*60)
        print("❌ PIPELINE FAILED")
        print("="*60)
        print(f"Error: {e}")
        
        print("\n💡 Troubleshooting:")
        print("   1. Check database connection in .env")
        print("   2. Verify tables exist: psql -d integration_db -f sql/schema.sql")
        print("   3. Check data files exist in data/")
        
        return False


if __name__ == '__main__':
    success = run_pipeline()
    
    if not success:
        exit(1)