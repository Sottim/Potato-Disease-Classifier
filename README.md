# Potato Disease Classifier
A lot of farmers stuggle with their potato field catching disease. I have used the Kaggle dataset to create a Deep learning model to predict if the potato plant is healthy or has caught with disease mainly : Early Blight and Late Blight. An individual can upload the potato leaf photo and find out the if the plant is healthy or if it is affected by the mentioned disease. 

I will deploy my model in Google cloud to this link so that everyone can access it.
Visit the link: https://potato-disease-classifier-wine.vercel.app/


This project is my approach to combine my learning in Web development and concepts of Deep Learning : Convolution Neural Network. 

## Instructions :
After cloning this repository, visit the frontend folder ``` 
npm run start  ``` to run the frontend. Run the  
``` 
main.py  ``` to activate the FastAPI server - a Python-based web framework.

## Python Setup:

1. Install Python 
2. Install Python packages

```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt

```

## Setup for ReactJS

1. Install Nodejs
2. Install NPM 
3. Install dependencies

```bash
cd frontend
npm install --from-lock-json
npm audit fix
```

4. Copy `.env.example` as `.env`.

5. Change API url in `.env`.

## Train the Model 

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village) and only keed 
2. Only keep folders related to Potatoes.

## Running the API

### We Use FastAPI

1. Get inside `api` folder

```bash
cd api
```

2. Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8000`

### Using FastAPI & TF Serve

1. Get inside `api` folder

```bash
cd api
```

2. Copy the `models.config.example` as `models.config` and update the paths in file.
3. Run the TF Serve (Update config file path below)

```bash
docker run -t --rm -p 8501:8501 -v C:/Code/potato-disease-classification:/potato-disease-classification tensorflow/serving --rest_api_port=8501 --model_config_file=/potato-disease-classification/models.config
```

4. Run the FastAPI Server using uvicorn
   For this you can directly run it from your main.py or main-tf-serving.py using pycharm run option (as shown in the video tutorial)
   OR you can run it from command prompt as shown below,

```bash
uvicorn main-tf-serving:app --reload --host 0.0.0.0
```

5. Your API is now running at `0.0.0.0:8000`

## Running the Frontend

1. Get inside `api` folder

```bash
cd frontend
```

2. Copy the `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.
3. Run the frontend

```bash
npm run start
```


2. Copy the `.env.example` as `.env` and update `URL` to API URL if needed.




