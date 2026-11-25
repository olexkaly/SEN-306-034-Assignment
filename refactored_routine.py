from result_module import calculate_total_score
from grading import calculate_grade
from grading import calculate_grade_point
from validation import validate_student


def process_result(
    name,
    registration_number,
    assignment,
    test,
    examination
):
    validate_student(name, registration_number)

    total = calculate_total_score(
        assignment,
        test,
        examination
    )

    return {
        "name": name,
        "total": total,
        "grade": calculate_grade(total),
        "grade_point": calculate_grade_point(total)
    }


def display_result(result):
    print(
        result["name"],
        result["total"],
        result["grade"]
    )


