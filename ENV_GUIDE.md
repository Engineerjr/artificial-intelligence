# Loading Environment Variables from .env Files in Python

## Overview
Environment variables allow you to store sensitive data (API keys, passwords, database URLs) outside your code. The `python-dotenv` library makes this easy.

## Installation
```bash
pip install python-dotenv
```

## Methods

### Method 1: Simple Loading
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file and sets environment variables
api_key = os.getenv("API_KEY")
```

### Method 2: Load Specific File Path
```python
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
```

### Method 3: Dictionary Approach (Non-invasive)
```python
from dotenv import dotenv_values

# Loads into dict without modifying os.environ
config = dotenv_values(".env")
api_key = config.get("API_KEY")
```

### Method 4: Class-based Configuration
```python
from dotenv import dotenv_values

class Config:
    def __init__(self, env_file=".env"):
        self.config = dotenv_values(env_file)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def get_bool(self, key, default=False):
        value = self.config.get(key, str(default)).lower()
        return value in ("true", "1", "yes")
    
    def get_int(self, key, default=0):
        try:
            return int(self.config.get(key, default))
        except (ValueError, TypeError):
            return default

config = Config(".env")
debug = config.get_bool("DEBUG")
port = config.get_int("PORT", 5000)
```

## .env File Format
```
# Comments start with #
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:pass@localhost/db
DEBUG=True
PORT=5000
```

## Best Practices
1. **Never commit .env to git** - Add `.env` to `.gitignore`
2. **Use defaults** - Always provide default values for optional variables
3. **Validate early** - Check required variables exist at app startup
4. **Type conversion** - Use helper methods for boolean/int conversion
5. **Separate configs** - Use different .env files for dev/test/prod

## Common Issues
- **Variables not loading?** - Ensure .env is in the correct directory
- **Import error?** - Run `pip install python-dotenv`
- **Override values?** - Use `load_dotenv(override=True)` if needed
