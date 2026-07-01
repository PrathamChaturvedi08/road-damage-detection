from typing import Dict
from typing import List

from pydantic import BaseModel


class Detection(BaseModel):

    class_name: str

    confidence: float

    bbox: List[float]


class Assessment(BaseModel):

    roadvision_score: int

    condition: str

    severity_score: int

    average_confidence: float

    total_detections: int

    damage_counts: Dict[str, int]


class PredictionResponse(BaseModel):

    filename: str

    annotated_image: str

    detections: List[Detection]

    assessment: Assessment

    processing_time: float

    status: str