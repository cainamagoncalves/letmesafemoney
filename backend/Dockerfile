FROM python:3.7-slim

# Set environment variables to prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .

# Installing dependencies
# Run APT and then clean up lists in one go: Makes image size smaller.
RUN apt-get update -yqq && apt-get install -y \
    git \
    python3-dev \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
