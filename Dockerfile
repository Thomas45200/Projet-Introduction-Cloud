FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Créer un utilisateur non-root
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app ./app

EXPOSE 5000

USER appuser

CMD ["python", "app/main.py"]
