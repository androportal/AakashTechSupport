=======================
Low Cost Linux Netbbok
======================

A **WebApp** to provide online *Technical Support* to the people using Netbook.

(Summer Internship 2014, Indian Institute of Technology, Bombay)

Clone
-----

- Make sure your Internet is working.
- Clone this repo by typing ::

    git clone https://github.com/androportal/AakashTechSupport.git


Installation
------------

- Install Virtual Environment using the following command ::

    sudo apt-get install python-virtualenv

- Create a Virtual Environment ::

    virtualenv /path/to/virtualenv

- Activate the virtualenv using the command ::

    source /path/to/virtualenv-name/bin/activate

- Change the directory to the `AakashTechSupport/` project using the command ::

    cd /path/to/AakashTechSupport

- Install pre-requisites using the command ::

    pip install -r Requirement.txt

  or you can also type ::

    easy_install `cat Requirement.txt`


Usage
-----

- Using mysql (For development server only). Though, we recommend to use `mysql` for deployment
  server. See `settings.py` file for usage.

- Create 'techsupport' database in 'MySQL'.

- Open `AakashTechSupport/AakashTechSupport/settings.py` file and do the following changes ::

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backend.mysql',
        'NAME'  : 'techsupport',
         # user and password is provide `AakashTechSupport/AakashTechSupport/top_secret.py` file.
         # for server deployment it will be blank 
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }

- For development on localhost open `AakashTechSupport/AakashTechSupport/wsgi.py` file and do following changes ::

    sys.path.append('/home/path/to/AakashTechSupport')
	
    activate_this = '/home/path/to/bin/activate_this.py'

- For development on localhost open `AakashTechSupport/AakashTechSupport/top_secret.py` file and do following changes ::

    db_user='root' (MySql username)
    
    db_pass = 'root' (MySql password)
	
- Populate the database using the following command ::

    cd /path/to/AakashTechSupport
    
    python manage.py syncdb

- Run the script populate.py which enters details of remote center into the table Tabletinfo from the details_of_rc.csv file ::
    
    python populate.py
    
- Run the script populate_category.py which enters lists of categories into the table categoriy from the details_of_rc.csv file ::
    
    python populate_category.py

- Start the server using the command ::

    python manage.py runserver


Contributing
------------

- Never edit the master branch.
- Make a branch specific to the feature you wish to contribute on.
- Send me a pull request.
- Please follow `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>`_
  style guide when coding in Python.

License
-------

GNU GPL Version 3, 29 June 2007.

Please refer this `link <http://www.gnu.org/licenses/gpl-3.0.txt>`_
for detailed description.
