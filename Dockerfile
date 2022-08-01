FROM python:3.9-alpine

EXPOSE 5000

WORKDIR /application
RUN python -m pip install --upgrade pip
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["/usr/local/bin/python3", "main.py"]