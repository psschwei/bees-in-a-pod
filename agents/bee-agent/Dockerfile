FROM python:3.12.9

WORKDIR /usr/arc/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY agent.py .

CMD ["fastapi", "run", "agent.py", "--port", "8080"]
