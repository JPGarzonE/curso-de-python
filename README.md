# Curso de python
Apuntes del curso básico de Python by Platzi

[Presentación principal del curso](https://static.platzi.com/media/public/uploads/curso-python-platzi_f311af99-c15a-48e3-983d-5e8c096012c0.pdf)

## ¿Qué es Python?

Python es un lenguaje de programación creado por Guido Van Rossum, con una sintaxis muy limpia, ideado para enseñar a la gente a programar bien. Se trata de un lenguaje interpretado o de script.

## Instalación

Existen dos versiones de Python que tienen gran uso actualmente, Python 2.x y Python 3.x, para este curso puedes utilizar cualquiera de las dos, pero yo Juan Pablo Garzón te recomendamos usar una versión 3.x ya que la 2.x no recibe más soporte.

Para instalar Python solo debes seguir los pasos dependiendo del sistema operativo que tengas instalado.

  - ### Windows
  
    Para instalarlo en Windows, debemos ir a https://www.python.org/downloads/release/python-2716/ el sitio reconocerá el sistema           operativo y te dará las opciones para descargar.

    Ejecuta el archivo que descargaste y sigue los pasos de instalación. Al finalizar vas a poder utilizar Python en tu computador y         estás listo para continuar con el curso.
  
  - ### MacOS
  
    La forma sencilla es tener instalado [homebrew](https://brew.sh/) y usar el comando:

      - #### Para instalar la Versión 2.7

            brew install python
            
      - #### Para instalar la Versión 3.x

            brew install python3
            
  - ### Linux
    
    Generalmente Linux ya lo trae instalado, para comprobarlo puedes ejecutar en la terminal el comando

      - #### Versión 2.7

            python -v

      - #### Versión 3.x

            python3 -v

    Si el comando arroja un error quiere decir que no lo tienes instalado, en ese caso los pasos para instalarlo cambian un poco de         acuerdo con la distribución de linux que estés usando. Generalmente el gestor de paquetes de la distribución de Linux tiene el           paquete de Python
    
    #### Si eres usuario de Ubuntu o Debian por ejemplo puedes usar este comando para instalar la versión 3.1:

        $ sudo apt-get install python3.1

    #### Si eres usuario de Red Hat o Centos por ejemplo puedes usar este comando para instalar python

        $ sudo yum install python

    Si usas otra distribución y eres usuario habitual de linux también puedes descargar los archivos para instalarlo manualmente.

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
