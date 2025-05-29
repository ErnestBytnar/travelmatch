FROM python:3.11-slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt /backend/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY backend/ /backend/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
