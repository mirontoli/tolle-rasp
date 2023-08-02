FROM python:3.10-bullseye
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY bot.py food.txt wisdom.txt .env ./
CMD ["python3", "bot.py"]

