FROM python:3.9-alpine

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .

EXPOSE 8081

CMD ["python", "app.py"]
