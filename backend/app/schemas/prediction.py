from pydantic import BaseModel


class PredictionResponse(BaseModel):

    filename: str

    detections: int

    processing_time: float

    status: str