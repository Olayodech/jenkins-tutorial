FROM arm64v8/python:3.9-slim

RUN useradd application
EXPOSE 5000

WORKDIR /home/mepot
ENV SQLALCHEMY_DATABASE_URI="sqlite:///data.db"

RUN python3 -m pip install --upgrade pip
RUN pip install pymysql
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

COPY requirements.txt requirements.txt
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements.txt 

# COPY application application
# COPY migrations migrations
# COPY main.py config.py boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP main.py
# RUN chown -R application:application ./
ENTRYPOINT [ "./boot.sh" ]

# ENTRYPOINT ["/usr/local/bin/python3", "main.py"]