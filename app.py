from fastapi import FastAPI, File, UploadFile
from src.predict import predict
import shutil

app = FastAPI()

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict(file_path)
    return {"disease": result}
