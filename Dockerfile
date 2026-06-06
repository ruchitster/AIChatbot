FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev

# Install Microsoft ODBC Driver 18
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/debian/12/prod.list \
    > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]