# APPLICATION SERVER

This Project teaches how to configure an application server using NginX and Gunicorn to serve a flask application

## Reference link for how to setup Gunicorn to serve a flask app
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04#step-4-configuring-gunicorn

After setting up gunicorn, follow the steps below to serve a specific project on the server. (In this case AirBnB_clone_v3)

Requirements:

1. Git clone your AirBnB_clone_v3
2. Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002
3. Nginx must serve this page both locally and on its public IP on port 80
4. To test your setup you should bind Gunicorn to api/v1/app.py
