from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:3000"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("./saved_model_versions/1")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]


@app.get("/ping")
async def ping():
    return "Hello, I am alive."

#data i.e image is coming in bytes
def read_file_as_image(data) -> np.array:
    #Image is read as an numpy array
    image = np.array(Image.open(BytesIO(data)))
    return image


#We pass the image of a potato to this function for prediction if it is diseased one or healthy
@app.post("/predict")
async def predict(
    #Upload the image to be tested. This will take the user input image and pass it to the model to predict 
    # if the potato leaf is healthy or with some disease based on how it has been trained upon
    file: UploadFile = File(...)

):
    #async and await comes very handy when mutiple users are accessing the model at the same time 
    image = read_file_as_image(await file.read()) #await lets 

    image_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(image_batch)

    #argmax returns the index of the largest value which corresponds to the index ->Class Name
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return{'class':predicted_class, 'confidence':float(confidence)}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

