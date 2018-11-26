# scores
Mudderscup score webapp

# Requirements (Linux)
python 3

install Django
`$ pip install django`

install  Virtualenv
`$ pip install virtualenv`

setup virtual environment in project director
`~/scores$ virtualenv venv`

install install package for the command mysql_config
`$sudo apt install libmariadbclient-dev`

install package for the command mysql_config
`$sudo apt install libmariadbclient-dev`

install mysql driver `$ pip install mysqlclient`

Set database user and password in settings.py

run `$ python manage.py migrate`

create an admin account `$ python manage.py createsuperuser`

start the server `$ python manage.py runserver`

create another user account on localhost:8000/admin/

use the scoring app on localhost:8000/score/index/
