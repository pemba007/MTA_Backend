"""Database settings, read from environment variables so credentials never live in git."""
import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_DATABASE = os.environ.get("DB_DATABASE", "mta")
