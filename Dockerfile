FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

CMD ["python", "-m", "hand.hand_application"]
