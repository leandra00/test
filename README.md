# myproject
This package was written using the django framework and dockerized.

## installation/running
To build the docker container:
`docker build . -t myapp`

To run the container:
`docker run -it -p 8000:8000 myapp`

Implemented endpoints:
* http://127.0.0.1:8000/
* http://127.0.0.1:8000/health
* http://127.0.0.1:8000/metadata

To run the tests:
(from within the container)
`python3 manage.py test`


## Risks with application/deployment:
* The app needs a proper webserver when going to prod. (Not the django default one, which is only intended for development.)
* In the pipeline, a docker push to somewhere appropriate after the build would be a good idea.
* Version number and description are hard coded in the metadata response. This could be more elegantly implemented using a manifest file perhaps. Or versioning using git branches/tags.
