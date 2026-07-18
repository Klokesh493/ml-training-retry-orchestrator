import csv
import sys


RETRYABLE = {"spot_interruption", "network_timeout", "transient_storage"}
QUARANTINE = {"data_contract", "schema_mismatch"}


def next_action(row):
    error = row["error_type"]
    retries = int(row["retries"])
    if error in QUARANTINE:
        return "quarantine"
    if error in RETRYABLE and retries < 3:
        return "retry"
    if error == "oom" and retries < 2:
        return "retry_with_more_memory"
    return "escalate"


def actions(rows):
    return [{"run_id": row["run_id"], "pipeline": row["pipeline"], "action": next_action(row)} for row in rows]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in actions(csv.DictReader(handle)):
            print(f'{item["run_id"]}: {item["action"]} {item["pipeline"]}')


if __name__ == "__main__":
    main(sys.argv[1])
