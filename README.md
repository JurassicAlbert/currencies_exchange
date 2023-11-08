# Currency Exchange REST API

## What i'm creating?
A RESTful web platform that provides a basic currency exchange service by interacting with an external API to fetch currency data and stores it in a local database.

## Why i'm creating this?
To offer a convenient way for users to access and exchange currency rates. The goal is to increase accessibility to currency exchange data and historical rates for various currency pairs.

## How i'm creating this?
### Technology Stack:
- Django (Python)
- SQLite (Database)

### Tools Used:
- Task Tracking Tools: Trello was utilized for tracking project tasks and progress.

### External API Used:
- https://app.currencyapi.com

## API Endpoints

### GET /currency/
- Fetches a list of all currencies present in the application database.

#### Admin Interface
- Allows listing of historical rates for specific currency pairs    .

## Base Requirements:
- Data is loaded from an external database, and currency and rates are stored in the local database.
- Used database: SQLite.
- Basic tests for endpoints.
- No authorization/authentication systems.

---

### Project Setup Steps

1.**Install Virtual Environment (Windows Command Prompt)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
2.**Set Environment Variables in .env File**
   ```bash
   SECRET_KEY=your_django_secret_key
   CURRENCY_API_KEY=your_currency_api_key
   ```

3.**Install Requirements from requirements.txt**
   ```bash
  pip install -r requirements.txt
   ```

4.**Apply Database Migrations (Django Command)**
   ```bash
  python manage.py makemigrations
  python manage.py migrate
   ```

5.**Populate Currencies Database**
   ```bash
  python manage.py loaddata currencies/fixtures/currencies.json
   ```

6.**Create Superuser Admin**
   ```bash
  python manage.py createsuperuser --email admin@admin.com --username admin
   ```

**Run test using pytest**
   ```bash
  pytest
   ```

**Run Server**
   ```bash
  python manage.py runserver
   ```


**Note:** This project was developed on Windows using Python 3.12.0.