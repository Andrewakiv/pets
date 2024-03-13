# Pets

Simple site to add, view different pets

## Quickstart

    sudo apt get update
    git clone https://github.com/Andrewakiv/pets.git
    cd src
      
    python3 -m venv venv   
    source venv/bin/activate
    pip3 install -r requirements.txt 
    
    cp .env.template .env
    
Run the app locally:

    python3 manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    gunicorn project.wsgi -b 0.0.0.0:8000