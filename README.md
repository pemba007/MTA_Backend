# MTA MetroCard System (Backend)

A Flask + PostgreSQL REST API that simulates the NYC MTA MetroCard fare system: issuing cards, adding balance, and processing turnstile swipes for MetroCards and debit/credit cards.

Built for a graduate Database Systems course. The React frontend lives in [mta_frontend](https://github.com/pemba007/mta_frontend).

## What it does

- **Issue cards.** Limited (pay-per-ride, with an initial balance) or Unlimited (valid for one month). Card numbers are generated UUIDs.
- **Fare logic on swipe.** Unlimited cards pass while unexpired. Limited cards are charged the $2.75 fare only if the balance covers it. The balance deduction and the payment record are written in one transaction and rolled back together on failure.
- **Debit/credit tap.** Records a pay-per-ride payment against a bank card.
- **Reporting.** Returns the most recent payments and the most recently issued cards.

## Tech

Python · Flask · PostgreSQL (psycopg2, parameterized queries) · Flask-CORS · Gunicorn (deployed to Heroku via `Procfile`)

## API

| Method | Endpoint | Body / params |
|---|---|---|
| `POST` | `/issue_metro_limited` | `{ "params": { "initialBalance": 20 } }` |
| `POST` | `/issue_metro_unlimited` | none |
| `GET`  | `/balance_check` | `?cardNumber=<id>` |
| `POST` | `/balance_add` | `{ "params": { "cardNumber": "<id>", "balanceToAdd": 10 } }` |
| `POST` | `/card_swipe_metro` | `{ "params": { "cardNumber": "<id>" } }` |
| `POST` | `/card_swipe_debit_credit` | `{ "params": { "cardNumber": "<bank card>" } }` |
| `GET`  | `/get_latest_payments` | none |
| `GET`  | `/get_latest_metrocards` | none |

## Data model

- `metrocards`: `CardNumber`, `IssuedOn`, `ExpiresOn`, `Balance`, `CardType` (`Limited` / `Unlimited`)
- `payment`: `TransactionID`, `CardNumber`, `TimeofPayment`, `PaymentType` (`Metrocard` / `Debit/Credit`)

## Running locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export DB_HOST=localhost DB_PORT=5432 DB_USER=postgres DB_PASSWORD=... DB_DATABASE=mta
flask run            # or: gunicorn wsgi:app
```
