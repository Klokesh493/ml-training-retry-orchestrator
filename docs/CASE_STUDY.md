# Ml Training Retry Orchestrator walkthrough

## Business problem

Classifies failed ML training jobs into retry, quarantine, or escalate actions based on failure mode and recent retry history.

## Reproduce the workflow

Run `python3 retry_orchestrator.py sample_failures.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
tr-101: retry recsys-training
tr-102: quarantine vision-training
tr-103: escalate ranking-training
```

The sample supplies these fields. `run_id`, `pipeline`, `error_type`, `retries`, `last_duration_minutes`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
