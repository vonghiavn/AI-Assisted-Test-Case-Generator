import json


def export(testcases, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            [tc.__dict__ for tc in testcases],
            f,
            indent=2,
            ensure_ascii=False
        )
