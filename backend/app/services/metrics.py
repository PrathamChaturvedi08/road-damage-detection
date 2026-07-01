CLASS_WEIGHTS = {

    "longitudinal_crack": 1,

    "transverse_crack": 3,

    "other_corruption": 4,

    "alligator_crack": 7,

    "pothole": 10,

}


def calculate_roadvision_score(
    severity_score,
    total_detections,
):

    penalty = (

        severity_score * 2

        +

        total_detections * 2

    )

    return max(100 - penalty, 0)


def get_condition(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 60:
        return "Fair"

    elif score >= 40:
        return "Poor"

    return "Critical"


def calculate_metrics(detections):

    damage_counts = {}

    severity_score = 0

    confidence_sum = 0.0

    for detection in detections:

        damage = detection["class_name"]

        confidence = detection["confidence"]

        damage_counts[damage] = (

            damage_counts.get(damage, 0) + 1

        )

        severity_score += CLASS_WEIGHTS[damage]

        confidence_sum += confidence

    total_detections = len(detections)

    average_confidence = (

        round(confidence_sum / total_detections, 3)

        if total_detections

        else 0.0

    )

    roadvision_score = calculate_roadvision_score(

        severity_score,

        total_detections,

    )

    condition = get_condition(

        roadvision_score

    )

    return {

        "damage_counts": damage_counts,

        "severity_score": severity_score,

        "average_confidence": average_confidence,

        "total_detections": total_detections,

        "roadvision_score": roadvision_score,

        "condition": condition,

    }