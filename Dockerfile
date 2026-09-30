FROM python:3.13-slim

WORKDIR /app

# Cache dependencies layer
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code
COPY app/app.py app.py

EXPOSE 8080

CMD ["python", "app.py"]
