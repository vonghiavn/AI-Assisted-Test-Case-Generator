from app.core.testcase_generator import TestCaseGenerator

def test_generate_basic():
    generator = TestCaseGenerator()
    testcases = generator.generate_from_requirement(
        "User can login using email and password"
    )
    assert len(testcases) > 0
