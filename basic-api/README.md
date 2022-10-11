# simple dockerized API
Based on FastAPI.
## Run locally
### Install dependencies 
`pip install -r requirements.txt`
### Run uvicorn server 
`uvicorn app.main:app --host 0.0.0.0 --reload --port 80`
## Run in container
### Build image
`docker build -t basic-api .`
### Run container
`docker run -d -p 80:80 basic-api`
## Access API
### Hello world
Go to http://localhost/helloworld
### Healthcheck
Go to http://localhost/health
### API documentation
Go to http://localhost/docs