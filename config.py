"""
Configuration management
Loads settings from environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # Database
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'integration_db')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    
    # API
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://jsonplaceholder.typicode.com')
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    
    # File paths
    DATA_DIR = 'data'
    CUSTOMERS_FILE = 'data/customers.csv'
    
    @property
    def db_connection_string(self):
        """PostgreSQL connection string"""
        return f"host={self.DB_HOST} port={self.DB_PORT} dbname={self.DB_NAME} user={self.DB_USER} password={self.DB_PASSWORD}"


# Create config instance
config = Config()