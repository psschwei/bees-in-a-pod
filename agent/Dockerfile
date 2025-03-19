FROM python:3.12.9

WORKDIR /usr/arc/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY simple.py .

CMD ["fastapi", "run", "simple.py", "--port", "8080"]
