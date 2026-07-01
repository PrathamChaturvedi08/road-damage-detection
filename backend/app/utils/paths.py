from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_ROOT.parent
    / "model"
    / "runs"
    / "baseline_yolo11n"
    / "weights"
    / "best.pt"
)

UPLOAD_DIR = PROJECT_ROOT / "uploads"

OUTPUT_DIR = PROJECT_ROOT / "outputs"

UPLOAD_DIR.mkdir(exist_ok=True)

OUTPUT_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}