
import importlib
try:
    FastAPI = importlib.import_module("fastapi").FastAPI
except ImportError:
    raise ImportError("FastAPI is not installed. Install it with: pip install fastapi uvicorn")
import sqlite3

app = FastAPI()

# This is the "Welcome" page
@app.get("/assets")
def get_assets():
    try:
        conn = sqlite3.connect('C:/Users/Zolta/assets.db')
        # This line is the magic—it makes rows act like dictionaries automatically
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()

        # 1. Ensure table exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_name TEXT,
                device_type TEXT,
                ip_address TEXT,
                status TEXT
            )
        ''')
        conn.commit()

        # 2. Fetch the data
        cursor.execute("SELECT * FROM assets")
        rows = cursor.fetchall()
        
        # 3. Build the list carefully
        asset_list = []
        for row in rows:
            asset_list.append(dict(row))

        conn.close()
        return {"assets": asset_list}
        
    except Exception as e:
        return {"error_message": str(e)}