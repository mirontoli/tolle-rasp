FROM python:3.10-bullseye
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
# cherry-pick the file to copy, otherwise rely on .dockerignore
COPY bot.py food.txt wisdom.txt ./
CMD ["python3", "bot.py"]

