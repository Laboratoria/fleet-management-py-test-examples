# Fleet Management Test Examples con Python / Flask


## Resumen del proyecto

Este proyecto es una implementación partial de [Fleet Management API](https://github.com/Laboratoria/curriculum/tree/main/projects/05-fleet-management-api)
en Python con Flask. Optamos por usar solo funciones en lugar de clases.

Puedes correr el app usando
`flask --app fleet_api/app run`

Y correr los tests con:
`pytest`
`pytest -v -m focus -s` - para enfocar un test con `@pytest.mark.focus`

### Tests

Corremos los tests con:
`pytest`
`pytest -v -m focus -s` - para enfocar un test con `@pytest.mark.focus`

Empezamos con [este recurso par armar los tests](https://flask.palletsprojects.com/en/3.0.x/testing/)
Usamos [`markers`](https://docs.pytest.org/en/stable/how-to/mark.html) para enfocar en algunos tests.

Estamos haciendo tests de taxis endpoints y trajectories endpoint,
primero usamos mocks y al final algunos ejemplos como usar un connecion de base de datos.

