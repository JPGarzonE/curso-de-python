# Curso de python
Apuntos del curso básico de Python by Platzi

## Entorno Virtual en Python:

En Python la comunidad comparte su código usando PyPi (python package index), es un repositorio para instalar módulos de la comunidad.

Con **pip install [nombre]** se puede instalar el paquete que deseas (para python 2).

Para hacerlo en Python 3 se usa **pip3 install [nombre]**

Podemos utilizar requirements.txt para ordenar los paquetes que requiere tu proyecto.

- ### Ambiente virtual

  - Nos permite encapsular un proyecto para poder instalar las versiones de los paquetes que se requieran sin tenerlos que instalar en todo el sistema operativo.
  
  - Es una buena práctica crear un ambiente virtual por cada proyecto de Python
en el que se trabaje.

  - Esto evita conflictos de paquetes en el intérprete principal.

- #### Instalar un entorno virtual
  Dentro de la carpeta de tu proyecto ejecutas
  ```
  pip3 install virtualenv
  ```

- #### Crear un entorno virtual
  Dentro de la carpeta de tu proyecto ejecutas
  ```
  // virtualenv [nombre_del_ambiente] (Por convención se llama normalmente 'venv')
  virtualenv venv
  ```
  
- #### Encender un entorno virtual
  Para Linux o Mac:
  ```
  source venv/bin/activate
  ```
  Para Windows (CMD):
  ```
  venv\Scripts\activate
  ```
  
 - #### Apagar un entorno virtual
  ```
  deactivate
  ```

- #### Ver las dependencias instaladas en el entorno virtual
  ```
  pip3 freeze
  ```

- #### EJ: Instalar flask
  ```
  pip3 install flask
  ```

- #### Instalar dependencias del archivo requirements
  Se puede crear un archivo como el que esta en la carpeta servidor de nombre requirements.txt que contenga que dependencias y que versiones se quieren instalar en el ambiente virtual y lo instala todoooo.
  
  Muy util en equipos de trabajo, cuando se tiene un repositorio en el que todos trabajan y se requiere que todos tengan las mismas caracteristicas y dependencias en su entorno virtual, simplemente se tiene ese archivo requierements.txt y todos lo bajan y ejecutan en sus ambientes virtuales
  ```
  pip3 install -r requirements.txt
  ```
  
 - #### Así se crea un archivo desde el cmd de Windows
    ```
    type nul > requirements.txt
    ```
    
 - ##### Saber si tienes instalado un paquete y en donde
    ```
    where [nombre_del_paquete]
    // Ej. Ver si esta instalado virtualenv
    where virtualenv
    ```
