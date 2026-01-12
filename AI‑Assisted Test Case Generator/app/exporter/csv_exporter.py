import csv


def export(testcases, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["ID", "Title", "Steps", "Expected Result", "Priority", "Type"]
        )

        for tc in testcases:
            writer.writerow(
                [
                    tc.id,
                    tc.title,
                    " | ".join(tc.steps),
                    tc.expected_result,
                    tc.priority,
                    tc.type,
                ]
            )
