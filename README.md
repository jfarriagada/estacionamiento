## virtualenv
```shell
$ pip install virtualenv
$ virtualenv venv_estacionamiento
$ cd venv_estacionamiento
$ source bin/activate
```

## project
```shell
$ git clone https://github.com/jfarriagada/estacionamiento.git  
$ cd estacionamiento/
$ pip install -r requirements.txt 
$ python manage.py migrate
$ python manage.py runserver
```

## API
http://localhost:8000/api-parking/?patent={patent}

## test
$ python manage.py test parkings

## coverage test
cargar el archivo `index.html`, en mi caso 
file:///Users/farriagada/dev/ve_demo/estacionamiento/htmlcov/index.html


