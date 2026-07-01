from pathlib import Path

from ultralytics import YOLO

from app.utils.paths import MODEL_PATH


model = YOLO(MODEL_PATH)


def predict(image_path: Path):

    results = model.predict(
        source=image_path,
        conf=0.25,
        verbose=False
    )

    return results[0]