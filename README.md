# IT Asset Inventory API 

A lightweight, high-performance REST API built to manage and track IT infrastructure assets (Routers, Servers, PCs). 

##  Tech Stack
* **Framework:** FastAPI (Python)
* **Database:** SQLite3
* **Server:** Uvicorn (ASGI)
* **Documentation:** Swagger UI (Auto-generated)

##  Features
* **Automated Table Creation:** Logic to self-initialize the SQLite database if it's missing.
* **RESTful Endpoints:** Standardized GET requests to retrieve asset inventory in JSON format.
* **Error Handling:** Built-in exception handling to provide clear feedback for database or connectivity issues.
* **Developer Friendly:** Fully interactive documentation via the `/docs` endpoint.

##  Getting Started

### 1. Installation
Ensure you have Python 3.10+ installed. Clone this repository and install the requirements:
```bash
pip install fastapi uvicorn

Navigate to your project folder in the terminal and start the server:

Powershell
python -m uvicorn main:app --reload

-View the Results
Once the terminal shows the server is running, open your browser to:

Interactive Documentation: http://127.0.0.1:8000/docs

Raw Asset Data: http://127.0.0.1:8000/assets

(Upcoming Features)
[ ] Asset Adder: Implementation of POST endpoints to add devices via the browser.

[ ] Health Check: Integrated ping logic to verify asset status in real-time.

[ ] Security: API Key authentication for secure access.
