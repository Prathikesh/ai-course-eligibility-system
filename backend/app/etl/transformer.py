def transform_eligibility(raw_data: dict):
    """
    Transforms raw eligibility text into structured rules
    """
    return {
        "university": raw_data["university"],
        "course_name": raw_data["course_name"],
        "min_passes": 2,
        "required_subjects": ["Mathematics"],
        "english_level": "S"
    }
