#!/bin/sh

# Run migrations
flask db init || true  # Allow this to fail if the migrations folder already exists
flask db migrate
flask db upgrade

# Start the Flask app
exec flask run --host=0.0.0.0