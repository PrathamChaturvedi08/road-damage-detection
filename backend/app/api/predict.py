from pathlib import Path
import shutil
import time

from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from app.schemas.prediction import PredictionResponse
from app.services.detector import predict
from app.utils.paths import ALLOWED_EXTENSIONS
from app.utils.paths import UPLOAD_DIR


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post(
    "/",
    response_model=PredictionResponse
)
def predict_image(file: UploadFile = File(...)):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Unsupported image format."
        )

    image_path = UPLOAD_DIR / file.filename

    with open(image_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    start = time.time()

    results = predict(image_path)

    end = time.time()

    return PredictionResponse(

        filename=file.filename,

        detections=len(results.boxes),

        processing_time=round(end - start, 3),

        status="Success"
    )