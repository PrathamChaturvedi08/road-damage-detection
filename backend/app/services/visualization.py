from pathlib import Path
from uuid import uuid4

import cv2


def save_prediction_image(
    prediction,
    filename: str,
    output_dir: Path
):

    annotated = prediction.plot()

    extension = Path(filename).suffix

    stem = Path(filename).stem

    unique_filename = (
        f"{stem}_{uuid4().hex[:8]}{extension}"
    )

    output_path = output_dir / unique_filename

    cv2.imwrite(
        str(output_path),
        annotated
    )

    return unique_filename