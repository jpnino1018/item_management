# Item Management API

A FastAPI-based REST API for managing items with name and price attributes. This simple service provides endpoints to create, retrieve individual items, and list all items. Data is stored in memory (non-persistent).

## Features
- Create new items with name and price
- Retrieve items by name
- List all items


## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Local Setup

### Using Python and virtual environment

1. Create and activate a virtual environment:
```powershell
# Create venv
python -m venv .venv

# Activate (PowerShell)
. .venv\Scripts\Activate.ps1

# Activate (Command Prompt)
.venv\Scripts\activate
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Start the server:
```powershell
uvicorn app.item_management:app --reload --host 127.0.0.1 --port 8000
```

### Using Docker

1. Build the container:
```powershell
docker build -t item-management .
```

2. Run the container:
```powershell
docker run -p 8000:8000 item-management
```

## API Usage

Once running, you can:

- Access the API documentation: http://127.0.0.1:8000/docs
- Access alternative API docs (ReDoc): http://127.0.0.1:8000/redoc


## API Endpoints

- `GET /items/`: List all items
- `POST /items/`: Create a new item
- `GET /items/{item_name}`: Get a specific item by name
