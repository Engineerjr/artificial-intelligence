import os
from dotenv import load_dotenv, dotenv_values
from pathlib import Path

# python-dotenv 1.2.3
# Read key-value pairs from a .env file and set them as environment variables

# ===== Method 1: Load .env and access via os.getenv() =====
# Loads variables into os.environ
load_dotenv()
API_KEY = os.getenv("API_KEY")
print(f"API_KEY: {API_KEY}")

# Get with default value if not found
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
print(f"SECRET_KEY: {SECRET_KEY}")

# ===== Method 2: Load from specific .env file path =====
# Useful if .env is not in the current directory
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# ===== Method 3: Load into dictionary without modifying os.environ =====
# Returns dict of env variables without altering environment
config = dotenv_values(".env")
print(f"\nLoaded config: {config}")

# ===== Method 4: Access specific variables from dictionary =====
database_url = config.get("DATABASE_URL", "sqlite:///default.db")
debug_mode = config.get("DEBUG", "False")
print(f"DATABASE_URL: {database_url}")
print(f"DEBUG: {debug_mode}")

# ===== Method 5: Create a class for better organization =====
class Config:
    """Load and manage environment variables"""
    
    def __init__(self, env_file=".env"):
        self.env_file = env_file
        self.config = dotenv_values(env_file)
    
    def get(self, key, default=None):
        """Get environment variable with optional default"""
        return self.config.get(key, default)
    
    def get_bool(self, key, default=False):
        """Get boolean environment variable"""
        value = self.config.get(key, str(default)).lower()
        return value in ("true", "1", "yes", "on")
    
    def get_int(self, key, default=0):
        """Get integer environment variable"""
        try:
            return int(self.config.get(key, default))
        except (ValueError, TypeError):
            return default

# Usage example
# app_config = Config(".env")
# api_key = app_config.get("API_KEY")
# debug = app_config.get_bool("DEBUG")
# port = app_config.get_int("PORT", 5000)