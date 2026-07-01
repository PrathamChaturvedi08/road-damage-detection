from typing import Dict
from typing import List

from pydantic import BaseModel


class Detection(BaseModel):

    class_name: str

    confidence: float

    bbox: List[float]


class PredictionResponse(BaseModel):

    filename: str

    annotated_image: str

    detections: List[Detection]

    damage_counts: Dict[str, int]

    severity_score: int

    total_detections: int

    processing_time: float

    status: str
    