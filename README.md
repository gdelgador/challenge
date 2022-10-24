# Challenge Project
-------------------------------

This project contain solution a challenge

## PreRequirements
- Docker
- Python 3.8 or more

## Deployment 

1. Install 'Postgrest' <code>docker-compose up</code>
2. Create conda enviroment <code>conda enviroment -n fast_api</code>
3. Activate enviroment <code>conda activate fast_api</code>
4. Install Package <code>pip install -r requirements.txt</code>
5. Execute All cells on notebook.ipynb

## FastApi Deploy
API program

1. From your terminar <code>cd project</code>
1. Execute <code>uvicorn main:app --reload</code> 
1. On your navegator go to the url **http://127.0.0.1:8000**
1. Api Documentation : **http://127.0.0.1:8000/docs**



