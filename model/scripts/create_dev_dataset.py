import random
import shutil
from pathlib import Path

# ===========================
# Configuration
# ===========================

TRAIN_IMAGES = 500
VAL_IMAGES = 100
TEST_IMAGES = 100

RANDOM_SEED = 42

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_DATASET = PROJECT_ROOT / "datasets" / "rdd2022"

DESTINATION_DATASET = PROJECT_ROOT / "datasets" / "rdd2022_dev"

# ===========================
# Clean Existing Development Dataset
# ===========================

if DESTINATION_DATASET.exists():

    print("Removing existing development dataset...")

    shutil.rmtree(DESTINATION_DATASET)

# ===========================
# Folder Structure
# ===========================

SPLITS = ["train", "val", "test"]

for split in SPLITS:

    (DESTINATION_DATASET / split / "images").mkdir(
        parents=True,
        exist_ok=True
    )

    (DESTINATION_DATASET / split / "labels").mkdir(
        parents=True,
        exist_ok=True
    )

# ===========================
# Copy Dataset Split
# ===========================

def create_split(split_name, sample_size):

    image_dir = SOURCE_DATASET / split_name / "images"
    label_dir = SOURCE_DATASET / split_name / "labels"

    destination_images = DESTINATION_DATASET / split_name / "images"
    destination_labels = DESTINATION_DATASET / split_name / "labels"

    image_files = list(image_dir.glob("*"))

    random.seed(RANDOM_SEED)

    sampled_images = random.sample(
        image_files,
        sample_size
    )

    copied = 0

    for image_file in sampled_images:

        label_file = label_dir / f"{image_file.stem}.txt"

        if not label_file.exists():
            print(f"Warning: Missing label for {image_file.name}")
            continue

        shutil.copy2(
            image_file,
            destination_images / image_file.name
        )

        shutil.copy2(
            label_file,
            destination_labels / label_file.name
        )

        copied += 1

    print(f"{split_name.capitalize():10} : {copied} images copied")


# ===========================
# Main
# ===========================

def main():

    create_split("train", TRAIN_IMAGES)

    create_split("val", VAL_IMAGES)

    create_split("test", TEST_IMAGES)

    print()

    print("=" * 50)
    print("Development dataset created successfully.")
    print(f"Location : {DESTINATION_DATASET}")
    print(f"Random Seed : {RANDOM_SEED}")
    print("=" * 50)

if __name__ == "__main__":

    main()