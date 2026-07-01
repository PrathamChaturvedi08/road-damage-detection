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

from app.services.metrics import calculate_metrics

from app.services.visualization import save_prediction_image

from app.utils.paths import ANNOTATED_DIR


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

    prediction = predict(image_path)

    detections = prediction["detections"]

    metrics = calculate_metrics(detections)

    annotated_filename = save_prediction_image(

        prediction["prediction"],

        file.filename,

        ANNOTATED_DIR

    )

    annotated_image = (
        f"/outputs/annotated/{annotated_filename}"
    )

    end = time.time()

    return PredictionResponse(

        filename=file.filename,

        annotated_image=annotated_image,

        detections=detections,

        inspection_summary={

            "roadvision_score":

            metrics["roadvision_score"],

            "condition":

            metrics["condition"],

            "severity_score":

            metrics["severity_score"],

            "average_confidence":

            metrics["average_confidence"],

            "total_detections":

            metrics["total_detections"],

            "damage_counts":

            metrics["damage_counts"],

        },

        processing_time=round(end - start, 3),

        status="Success",

    )