# ------------ Dockerfile ------------
FROM python:3.12-slim

# 1. Instalar build-deps mínimos; se limpian después
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# 2. Copiamos el código de la aplicación
WORKDIR /app
COPY . /app

# 3. Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el script que espera a la BD
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

# 5. Puertos y comando de arranque
EXPOSE 8000
CMD ["/wait-for-db.sh"]
# ------------------------------------
