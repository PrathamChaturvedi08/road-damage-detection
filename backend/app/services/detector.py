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

    result = results[0]

    detections = []

    for box in result.boxes:

        class_id = int(box.cls[0])

        detections.append({

            "class_id": class_id,

            "class_name": result.names[class_id],

            "confidence": round(float(box.conf[0]), 3),

            "bbox": [
                round(float(x), 2)
                for x in box.xyxy[0]
            ]

        })

    return detections