# stunning-computing-machine
 - Anaconda
   - Install anaconda
   - Create anaconda environment basicwebsite

 - Django
   - Activate anaconda environment basicwebsite
   - pip install django
   - django-admin startproject mysite

 - Gunicorn
   - Activate anaconda environment basicwebsite
   - Install gunicorn in the environment
   - https://docs.gunicorn.org/en/latest/deploy.html - Systemd
   - Make changes to gunicorn.service, gunicorn.socket as per repo files
   - Enable the gunicorn service

 - Nginx
   - sudo apt-get install nginx
   - copy the basicwebsite (nginx conf) to /etc/nginx/sites/enabled/
   - remove any other sites from that directory
   - Enable the nginx service

 - Testing
   - curl http://localhost/articles/2003/
   - curl http://localhost/articles/2004/
   - curl http://localhost/articles/2004/06/
   - http://35.223.113.55/articles/2003/ from browser works
