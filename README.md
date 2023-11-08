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

**Note:** This project was developed on Windows using Python 3.11.2.