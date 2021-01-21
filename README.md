# Kickstart

Clone this project to "kickstart" your web application development with Flask / Bootstrap, on a responsive design base.


## Installation
```sh
git clone https://github.com/Alarid/flask-bootstrap-kickstart.git
cd <directory>
pip install -r requirements.txt
flask db migrate
```

Create a file "<filename>.env" with the need env variables, for example:
```sh
SECRET_KEY=a-really-long-and-unique-key-that-nobody-knows
MAIL_SERVER=localhost
MAIL_PORT=8025
```


## Run the web application
To launch the application, simply use:
```sh
flask run
```
To edit the default application name, change the **APP_NAME** variable in the configuration file (*config.py*).


## Manage translations
```sh
flask translate init LANG   # to add a new language
flask translate update      # to update all language repositories
flask translate compile     # to compile all language
```

# Licence
![Licence](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
