def validate(testcases):
    """
    Remove low-quality test cases
    """
    valid = []
    for tc in testcases:
        if (
            tc.title
            and len(tc.steps) >= 2
            and tc.expected_result
            and tc.priority in ["Low", "Medium", "High"]
        ):
            valid.append(tc)
    return valid
