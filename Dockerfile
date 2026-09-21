FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app-sql.py .

EXPOSE 5000

CMD ["python", "app-sql.py"]