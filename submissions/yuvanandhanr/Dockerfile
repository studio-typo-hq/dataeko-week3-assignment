FROM python:3.13-slim

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
# If only app.py changes, pip install won't need to run again
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/app.py .

# Document which port the app uses (informational only)
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
