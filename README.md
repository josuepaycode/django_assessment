# Django Assessment

## Intro

Esta aplicación usa python 3.8.13 y Django 4.1.3

## Listado de tareas 

### Tarea #1

#### CRUD de clientes y pagos de cliente

crear 3 tablas, customers, payments_customers, administrators

1. Estructura de la tabla customers

   - id
   - name
   - paternal_surname
   - email

2. Estructura de la tabla payments_customers

   - id
   - amount
   - customer_id
   - product_name
   - quantity

3. Estructura de la tabla customers

   - id
   - name
   - password
   - rol `[administrator,super_administrator]`

Crear 2 registros dummy en la tabla administrators uno con cada rol 
#### Usuarios Creados
**usuario**: administrador **contraseña**: administrador **rol**: administrador

**usuario**: super_administrador **contraseña**: super_administrador **rol**: super_administrador

Crear login usando la tabla administrators.

   - Cuando el rol sea super_administrator, permitira editar, borrar y crear clientes
   - Cuando el rol sea administrator solo se listaran los usuarios y pagos del usuario.
#### El login se podra encontrar en el siguiente path

http://localhost:8000/users/login/


Crear CRUD para la tabla customers.

   - Cada ves que se inserte un registro en la tabla customers se debe crear uno o varios registros dummy en la tabla payments_customers

Crear vistas de listado

   - listado de customers
   - listado de payments_customers


### Tarea #2

Crear un API REST

   - Implementar modulo de autenticacion usando la tabla administrators
   #### La autenticacion se podra encontrar en el siguiente path 
   http://127.0.0.1:8000/users/api-token-auth/

   #### Coleccion de postman para ejemplificar el consumo de los servicios
   https://www.postman.com/descent-module-cosmonaut-98032247/workspace/public/collection/24845288-801fceca-14c7-46ca-b61c-3769f8a5d99a?ctx=documentation
   - Endpoint que listara customers
   - Endpoint que listara payments_customers
   - Endpoint para editar customers
   - Endpoint para eliminar customers
   - Endpoint para insertar customers
   - Solo los administradores con el rol super_administrator podran ejecutar creciones, ediciones y eliminaciones

