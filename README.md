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
   - Make changes to gunicorn.service as per repo files
   - Enable the gunicorn service

 - Nginx
   - sudo apt-get install nginx
   - copy the basicwebsite (nginx conf) to /etc/nginx/sites/enabled/
   - remove any other sites from that directory
   - Enable the nginx service

 - https support
   - obtain domain name from godaddy / google domains
   - Point this domain name to the external IP provided
   - Use the certbot from letsencrypt to generate the certificates
   - nginx config with ssl for let's encypt certs
     - https://gist.github.com/nrollr/9a39bb636a820fb97eec2ed85e473d38
     - replace the domain.com with the domain name obtained
   - openssl dhparam -out dhparam4096.pem 4096. Copy the pem file to /etc/ssl

 - Testing
   - http://api.kubelearning.com/articles/2003/ from browser works
   - https://api.kubelearning.com/articles/2003/ from browser works

 - postgresql
   - Install psycopg2-binary
   - export the below ENV variables for the bare metal to run..
       DB_NAME=app, DB_HOST=localhost, DB_PASSWORD=supersecretpassword, DB_USER=postgres
   - Have provided the above variables in gunicorn.env
   - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
   - change the password on the db to 'supersecretpassword'
 
 - Deployment
   - Bare Metal
       - Enable the gunicorn service
       - Enable the nginx service
   - Unit test
       - docker-compose run mysite sh -c "python manage.py test && flake8"
   - Docker
       - docker-compose -f docker-compose.prod.yml up
       - Enable the nginx service

