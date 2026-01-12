import json
from app.ai.llm_client import LLMClient
from app.ai.prompt_templates import TESTCASE_PROMPT
from app.models.testcase import TestCase


class TestCaseGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def generate_from_requirement(self, requirement: str):
        prompt = TESTCASE_PROMPT.format(requirement=requirement)
        raw = self.llm.generate(prompt)

        data = json.loads(raw)
        testcases = []

        for i, tc in enumerate(data, start=1):
            testcases.append(
                TestCase(
                    id=f"TC-{i:03}",
                    title=tc["title"],
                    description="",
                    preconditions=[],
                    steps=tc["steps"],
                    expected_result=tc["expected_result"],
                    priority=tc["priority"],
                    type=tc["type"],
                )
            )

        return testcases
