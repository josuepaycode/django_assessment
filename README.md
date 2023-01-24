# Django Assessment

## Prerequisitos

- [Docker](https://docs.docker.com/get-docker/)

## Ejecución del proyecto

Para ejecutar este proyecto por primera vez, solo necesitas ejecutar el siguiente comando:

```bash
docker compose up --build
```

Posterior a eso puedes correrlo con:

```bash
docker compose up
```

## Poblar la base de datos

```bash
docker-compose run web python manage.py shell
```
```python
from common.scripts.populate_db import run
run()
```

## Ejecutar los tests

Se probaron cosas basicas, como la correcta respuesta de los endpoints y el match de los datos

```bash
  docker-compose run web python manage.py test .
```

## Listado de tareas 

### Tarea #1

#### CRUD de clientes y pagos de cliente

crear 3 tablas, customers, payments_customers, administrators

1. Estructura de la tabla customers

   - id
   - name
   - paternal_surname
   - email

```bash
El modelo para está tabla fue creado en el app customers
```

2. Estructura de la tabla payments_customers

   - id
   - amount
   - customer_id
   - product_name
   - quantity

```bash
El modelo para está tabla fue creado en el app payments
```

3. Estructura de la tabla customers

   - id
   - name
   - password
   - rol `[administrator,super_administrator]`

```bash
Para esta tabla reutilice el modelo User que ofrece Django, para identificar el rol utilice las banderas 
banderas que ofrece:
```

```python
is_staff: administrator
is_superuser: super_administrator
```

Crear 2 registros dummy en la tabla administrators uno con cada rol 

Crear login usando la tabla administrators.

   - Cuando el rol sea super_administrator, permitira editar, borrar y crear clientes
   - Cuando el rol sea administrator solo se listaran los usuarios y pagos del usuario.

```bash
Para crear este login reutlice el que Django ofrece por defecto en su admin:
http://localhost:8000/admin/
```
```python
Para los permisos, se utiliza la clase Permission que ofrece django en conjunto con las banderas
```
´´´python
is_staff: administrator
is_superuser: super_administrator
´´´

Crear CRUD para la tabla customers.

   - Cada ves que se inserte un registro en la tabla customers se debe crear uno o varios registros dummy en la tabla payments_customers

```bash
Se valida en el metodo save() del modelo Customer si el registro es nuevo, en caso de serlo se agregan sus respectivos dummies
a Payments.
```

Crear vistas de listado

   - listado de customers
   - listado de payments_customers

```
Al igual que para el login, se ocupo el django admin para validar lo que el usuario puede hacer, se restringio sus permisos para solo consultar registros y para el usuario superadmin, se permitió realizar cualquier acción.
```

### Tarea #2

Crear un API REST

   - Implementar modulo de autenticacion usando la tabla administrators

```bash
Se implemento JWT para la autenticación de usuarios al API.
```

   - Endpoint que listara customers
   - Endpoint que listara payments_customers
   - Endpoint para editar customers
   - Endpoint para eliminar customers
   - Endpoint para insertar customers
   - Solo los administradores con el rol super_administrator podran ejecutar creciones, ediciones y eliminaciones

```bash
Para cada uno de los endpoints se puede recurrir al API Doc que brinda Swagger configurada en el proyecto,
permite interactuar con todos los endpoints.
```

- [Swagger](https://drf-yasg.readthedocs.io/en/stable/)
- [SwaggerLocal](http://localhost:8000/api/doc/)