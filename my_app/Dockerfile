FROM python:slim

WORKDIR /app

# Copy requirements.txt separately to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY main.py /app/

CMD ["python3", "main.py"]
