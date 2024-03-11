# Fleet Management Software API

## Índice

* [1. Preámbulo](#1-preámbulo)
* [2. Resumen del proyecto](#2-resumen-del-proyecto)
* [3. Criterios de aceptación del proyecto](#5-criterios-de-aceptación-del-proyecto)
* [4. Pistas, tips y puntos complementarias](#7-pistas-tips-y-lecturas-complementarias)
* [5. Funcionalidades opcionales](#8-funcionalidades-opcionales)

***

## 1. Resumen del proyecto

Este proyecto es una implementación de [Fleet Management API](https://github.com/Laboratoria/curriculum/tree/main/projects/05-fleet-management-api)
en Python con Flask. Optamos por usar solo funciones en lugar de clases.

Puedes correr el app usando
`flask --app fleet_api/app run`

Y correr los tests con:
`pytest`
`pytest -v -m focus -s` - para enfocar un test con `@pytest.mark.focus`

Cumplimos los siguientes hitos:

## 2. Criterios de aceptación del proyecto (Hitos)

### Definición del producto

#### [Historia de usuario 1] Cargar información a base de datos

Yo, como desarrolladora, quiero cargar la información almacenada hasta ahora en
[archivos sql](https://drive.google.com/file/d/1T5m6Vzl9hbD75E9fGnjbOiG2UYINSmLx/view?usp=drive_link)
en una base de datos PostgreSQL, para facilitar su consulta y análisis.

##### Notas de implementación

Esta historia no implica codigo y es mas de instalacion de base de datos,
cargando los SQLs, y verificando la connecion de base de datos.
Usamos Vercel. Link to vercel.

***

##### [Historia de usuario 2] Endpoint listado de taxis

Yo como clienta de la API REST requiero un _endpoint_ para
listar todos los taxis.

##### *Notas de implementación

Nuestro endpoint fue `api/taxis`
Acepta `page` y `per_page` [request args](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.args), y estamos dando valores por defecto con [`get`](https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/#werkzeug.datastructures.MultiDict.get)

***

#### [Historia de usuario 3] Endpoint historial de ubicaciones

Yo como clienta de la API REST requiero un _endpoint_ para
consultar todas las ubicaciones de un taxi dado el id y una fecha.

El endpoint es `/api/taxis/[id]/locations?date=`
Pensamos que `id` seria  param requerido y podemos paginar por defecto.
El `date` sirve como filtro, también es requerido.
Acepta `page` y `per_page` [request args](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.args), y estamos dando valores por defecto con [`get`](https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/#werkzeug.datastructures.MultiDict.get)

Usamos un url dinamica con un [variable rule](https://tedboy.github.io/flask/quickstart/quickstart4.html#variable-rules) y con converter para `taxi_id` es un `int`

***

#### [Historia de usuario 4] Endpoint última ubicación

Yo como clienta de la API REST requiero un _endpoint_ para
consultar la última ubicación reportada por cada taxi.

##### Notas de implementación

Endpoint es `/api/taxis/locations/` que
devuelva el ultimo trajectory por cada taxi.

Acepta `page` y `per_page` [request args](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.args), y estamos dando valores por defecto con [`get`](https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/#werkzeug.datastructures.MultiDict.get)

***

## 4. Pistas, tips y puntos complementarias

Algunos links que nos ayudo:

* [Getting started flask testing](https://flask.palletsprojects.com/en/3.0.x/testing/)
* [Exceptions de db](https://www.psycopg.org/docs/errors.html)
* [Exception handling in Flask](https://flask.palletsprojects.com/en/3.0.x/errorhandling/#generic-exception-handlers)
* [Flask esta basado en el WSGI lib Werkzeug](https://https://werkzeug.palletsprojects.com/en/3.0.x/.palletsprojects.com/en/3.0.x/)

Algunas pistas:

* En los tests, usamos `name` con los mocks y empieza con `_` para evitar errores de linter
* Recuerda con los tests, los patches [esta aplicado en reverse orden con los args](https://stackoverflow.com/a/47042383)

### Blueprints y funcionalidades avanzada en Flask

Puedes usar [blueprints](https://www.google.com/search?q=flask+blueprints&rlz=1C5CHFA_enUS786US786&oq=flask+blueprints&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDI2NDlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8) para organizar el proyecto, pero no usamos en este implementación.

### Tests

Corremos los tests con:
`pytest`
`pytest -v -m focus -s` - para enfocar un test con `@pytest.mark.focus`

Empezamos con [este recurso par armar los tests](https://flask.palletsprojects.com/en/3.0.x/testing/)
Usamos [`markers`](https://docs.pytest.org/en/stable/how-to/mark.html) para enfocar en algunos tests.

### Documentación con swagger

Flask con ningun otro extension no apoya swagger muy facil, hay otro Flask-REST etc
que tiene este mas 'out of the box'.
Usamos [`apispec-webframeworks.flask`](https://github.com/marshmallow-code/apispec-webframeworks)
para ayudar con los specs.

## 5. Funcionalidades opcionales

Aun hay que implementar las funcionalidades opcional.
