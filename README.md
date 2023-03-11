# Django Assessment


## Requerimientos

Para correr el proyecto se debe contar con docker-compose ya instalado

La aplicación usa python 3.8.13 definido en el Dockerfile

En requirements se pueden observar las dependencias con sus respectivas versiones


## Instalación y ejecución

Ejecutar el siguiente comando para construir el contenedor y levantar el servicio

```bash
docker-compose up -d --build
```

### Servidor de backend
El servidor se levantará en el puerto 8000

La documentación de los endpoints se puede consultar accediendo en `http://localhost:8000/swagger`

![Screenshot from 2023-03-10 19-18-22](https://user-images.githubusercontent.com/9125861/224457186-86b64a99-13aa-43f1-9aed-5cfbdcc7b9f6.png)


### Testing
Se agregaron tests para comprobar el correcto funcionamiento de:
- CRUD Customers
- Registro de Administradores
- Login para obtener un Token
- Permisos basados en Roles sobre endpoints de Customers

![Screenshot from 2023-03-10 17-30-28](https://user-images.githubusercontent.com/9125861/224457202-5cebe837-6e5e-43ce-8ee1-6e114079af21.png)

