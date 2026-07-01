from pathlib import Path

import cv2


def save_prediction_image(
    prediction,
    filename: str,
    output_dir: Path
):

    annotated = prediction.plot()

    output_path = output_dir / filename

    cv2.imwrite(
        str(output_path),
        annotated
    )

    return output_path