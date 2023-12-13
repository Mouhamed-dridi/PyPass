FROM python:3-slim

COPY app.py requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
