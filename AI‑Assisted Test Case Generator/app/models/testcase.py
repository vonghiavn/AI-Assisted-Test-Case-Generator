from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
id: str
title: str
description: str
preconditions: List[str]
steps: List[str]
expected_result: str
priority: str
type: str # positive / negative / edge / security