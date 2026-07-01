CLASS_WEIGHTS = {

    "longitudinal_crack": 1,

    "transverse_crack": 2,

    "alligator_crack": 3,

    "other_corruption": 2,

    "pothole": 5

}


def calculate_metrics(detections):

    damage_counts = {}

    severity_score = 0

    for detection in detections:

        damage = detection["class_name"]

        damage_counts[damage] = damage_counts.get(
            damage,
            0
        ) + 1

        severity_score += CLASS_WEIGHTS[damage]

    total_detections = len(detections)

    return {

        "damage_counts": damage_counts,

        "severity_score": severity_score,

        "total_detections": total_detections

    }