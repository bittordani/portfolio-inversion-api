# 📈 Portfolio de Inversión con FastAPI

Proyecto desarrollado con **FastAPI** y **MariaDB**, desplegado mediante **Docker** y orquestado con **Docker Compose**. Permite gestionar un portfolio de inversiones en bolsa (CRUD) y demuestra buenas prácticas de desarrollo y despliegue.

---

## 🔧 Tecnologías y herramientas

* [FastAPI](https://fastapi.tiangolo.com/): Framework web moderno y rápido
* [SQLAlchemy](https://www.sqlalchemy.org/): ORM para comunicación con la base de datos
* [MariaDB](https://mariadb.org/): Base de datos relacional
* [Docker](https://www.docker.com/): Contenerización de la app y la base de datos
* [Docker Compose](https://docs.docker.com/compose/): Orquestación multi-contenedor
* `wait-for-db.sh`: Script que espera a que la BBDD esté lista antes de arrancar FastAPI

---

## 🏙þ Estructura del proyecto

```
portfolio-inversion-api/
├── app/                   # Módulos y lógica de negocio
│   └── database.py        # Conexión SQLAlchemy
│   └── main.py            # Entrada principal de la API
│   └── modelos.py         # Modelo SQLAlchemy
│   └── schemas.py         # Validación Pydantic
├── requirements.txt       # Dependencias Python
├── Dockerfile             # Imagen personalizada de FastAPI
├── docker-compose.yml     # Orquestador de servicios
├── wait-for-db.sh         # Script bash para sincronizar el arranque
└── README.md              # Este archivo
```

---

## 🚀 Cómo ejecutar el proyecto

1. **Clona el repositorio y entra en el proyecto**:

```bash
git clone <repo-url>
cd portfolio-inversion-api
```

2. **Crea y levanta los contenedores**:

```bash
sudo docker compose up --build
```

Esto crea dos contenedores:

* `mariadb`: con la base de datos `inversiones_db`
* `fastapi-api`: la API corriendo en [http://localhost:8080](http://localhost:8080)

3. **Accede a la documentación interactiva**:

* Swagger: [http://localhost:8080/docs](http://localhost:8080/docs)
* Redoc: [http://localhost:8080/redoc](http://localhost:8080/redoc)

---

## 🚫 Detener el proyecto

Para detener los contenedores:

```bash
sudo docker compose down
```

---

## 📂 Volumen de persistencia

La base de datos usa un volumen llamado `mariadb_data`. Gracias a esto:

* Los datos NO se pierden aunque detengas o reinicies Docker.
* Se mantienen los registros insertados en la tabla `inversiones`.

---

## 🧹 Comprobación manual de datos

Puedes comprobar los datos insertados conectándote a la base de datos con `phpMyAdmin` (si lo tienes), o desde el terminal:

```bash
docker exec -it mariadb mariadb -u fastapi_user -p
```

---

## 🧲 Autor

* **Víctor Daniel Martínez**
* Linkedin: www.linkedin.com/in/victor-daniel-martinez-martinez
* Proyecto realizado para el módulo de Contenedores y Virtualización del Máster en IA, Cloud Computing & DevOps de PontIa.tech

---

