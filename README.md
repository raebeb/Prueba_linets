# Prueba Linets

Desarrollo evaluación tecnica

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


### Pre-requisitos 📋

- Docker
- Python 3.x


### Ejecución 🔧

1. Clonar el proyecto y entrar a la carpeta prueba_linets
2. ejecutar en consola ``` docker-compose up -d ``` en este paso se instalaran las dependencias detalladas en requirements.txt
3. En el navegador entrar a ``` localhost:8000/ ``` para ir a la pagina principal
4. Las url de los endpoint son las siguientes:
  - ApiOverview: ``` localhost:8000/generate_csv/api_view/ ```
  - Consultar datos: ``` localhost:8000/generate_csv/product-list/ ```
  - Agregar datos: ``` localhost:8000/generate_csv/product-create/ ```
  - Ver detalle de un producto: ``` localhost:8000/product-detail/<sku>/ ```


## Construido con 🛠️

Se utilizaron las siguientes herramientas para el desarrollo del proyecto

* [Docker](https://www.docker.com/products/docker-desktop) - Manejador de contenedores
* [Python](https://www.python.org/downloads/) - Lenguaje de programación 
* [Django](https://www.djangoproject.com/download/) - Framework utilizado para desarrollo de la aplicacion web
* [DjangoREST framework](https://www.django-rest-framework.org/tutorial/quickstart/) - Framework utilizado para desarrollo de api


## Versionado 📌

Se utilizo [Git](https://git-scm.com/) para el control de versiones y github como repositorio remoto. 

## Autor ✒️

* **Francisca Osores** - *Trabajo Inicial* - [raebeb](https://github.com/raebeb)


---
⌨️ con ❤️ por [Raebeb](https://github.com/Raebeb) 
