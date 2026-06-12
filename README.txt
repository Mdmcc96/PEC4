PEC 4-

María del Mar Correro Cabrera


ESTRUCTURA Y ORGANIZACIÓN DE LAS CARPETAS
PEC4/
├── src/
│   ├── main.py
│   ├── data/
│   │   └── LaLiga_Matches.csv
│   └── exercises/
│       ├── __init__.py
│       ├── config.py
│       ├── ex1.py
│       ├── ex2.py
│       ├── ex3.py
│       ├── ex4.py
│       ├── ex5.py
│       ├── ex6.py
│       └── ex7.py
├── tests/
│   └── test.py
├── doc/
├── screenshots/
├── Requirements.txt
├── LICENSE
└── README.md

INSTALACIÓN ENTORNO DE TEST
Para crear el entorno en el que ejecutaremos el test del ejercicio 6, hay que ejecutar los siguientes comandos en orden:
1- python -m venv venv
2- Activa el entorno virtual (en este caso en Windows):
.\.venv\Scripts\Activate.ps1

3- Instala las dependencias:

pip install -r requirements.txt

Las dependencias también puedes instalarlas usando el siguiente comando:  pip install pandas matplotlib networkx pytest



EJECUCIÓN DEL PROYECTO:
Mostrar ayuda:

python src/main.py -h

Para ejecutar de forma secuencial los ejercicios, usaremos el siguiente comando:
python src/main.py -ex NUM_EJERCICIO

Por ejemplo, para ejecutar hasta el ejercicio 7:
python src/main.py -ex 7


LINTING
En primer lugar, instala pylint usando el siguiente comando:

pip install pylint

Para ejecutar pylint, usa el siguiente comando estando en la carpeta src:

pylint .


CÓMO GENERAR LA DOCUMENTACIÓN
En primer lugar, instala pdoc:

pip install pdoc

Genera la documentación ejecutando el siguiente comando:

pdoc src/exercises -o doc

La documentación generada se almacenará en la carpeta doc/.




EJECUCIÓN DE TEST
Primero instala pytest:

pip install pytest

Ejecutar los tests:

pytest tests/
Dependencias

Las dependencias necesarias para ejecutar el proyecto se encuentran en el fichero requirements.txt.

Licencia

Este proyecto se distribuye bajo la licencia Apache. Consulta el fichero LICENSE para más información.



SUBIR EL PROYECTO GitHub

Inicia repositorio:

git init

Añade los archivos:

git add .

Crear commit:

git commit -m "PEC4"

Vincular repositorio remoto:

git remote add origin https://github.com/USUARIO/REPOSITORIO.git

Subir proyecto:

git branch -M main
git push -u origin main
