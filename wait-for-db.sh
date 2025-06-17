#!/usr/bin/env bash
echo "⌛ Esperando a la BD en $DB_HOST:$DB_PORT ..."
until mysqladmin ping -h"$DB_HOST" -P"$DB_PORT" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
  sleep 2
done
echo "✅ BD disponible, lanzando Uvicorn"
exec uvicorn app.main:app --host 0.0.0.0 --port 8080

