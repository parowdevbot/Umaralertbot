FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app.main:main", "--workers", "1", "--threads", "1", "--timeout", "60"]
