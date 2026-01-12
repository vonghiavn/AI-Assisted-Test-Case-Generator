from app.core.testcase_generator import TestCaseGenerator
from app.core.validator import validate
from app.exporter.json_exporter import export


requirement = """
User can login using email and password.
"""


generator = TestCaseGenerator()
testcases = generator.generate_from_requirement(requirement)
testcases = validate(testcases)


export(testcases, "output_testcases.json")
print(f"Generated {len(testcases)} test cases")