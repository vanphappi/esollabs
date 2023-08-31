FROM python:3.10.12-slim-bullseye
WORKDIR /app
COPY requirements.txt .
COPY lib/requirements.txt /app/lib/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r lib/requirements.txt
COPY . .
EXPOSE 5001
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5001"]
