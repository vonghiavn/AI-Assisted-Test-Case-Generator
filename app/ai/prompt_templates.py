TESTCASE_PROMPT = """
You are a senior QA engineer.


Given the following requirement, generate comprehensive software test cases.


Requirement:
{requirement}


Rules:
- Cover positive, negative, edge, and security cases
- Use clear steps
- Return result in JSON list
- Each test must include: title, steps, expected_result, priority, type
"""