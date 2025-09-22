# Django CSV Upload API

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## Endpoint
- **POST** `/upload-csv/`
- Upload a CSV file with columns: `name,email,age`

## Example
Request: 
- POST /upload-csv/
- file: sample.csv

Response:

- {
  "records_saved": 2,
  "records_rejected": 2,
  "errors": [...]
}