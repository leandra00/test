This package was written using the django framework and dockerized.

To build the docker container:
docker build . -t myapp

To run the container:
docker run -it -p 8000:8000 myapp

Implemented endpoints:
http://120.0.0.1:8000/
http://120.0.0.1:8000/health
http://120.0.0.1:8000/metadata

To run the test suits:
(from within the container)
python3 manage.py test



Risks with application/deployment:
Need a proper webserver when going to prod. (Don't use the django development one.)
