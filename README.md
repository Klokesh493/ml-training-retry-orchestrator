# ML Training Retry Orchestrator

Classifies failed ML training jobs into retry, quarantine, or escalate actions based on failure mode and recent retry history.

Focus: MLOps, training orchestration, SRE incident reduction.

Portfolio framing: Apple-scale client-style AI platform project using synthetic data only.

## Run

```bash
python3 retry_orchestrator.py sample_failures.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

Unconditional retries can waste training capacity and repeat permanent failures. Operators need a bounded policy for retry, quarantine, or escalation.

## Project walkthrough

```mermaid
flowchart LR
    A["Training failure and retry count"]
    B["Apply failure-type policy and retry cap"]
    C{"Eligible for retry?"}
    D["Retry or retry with more memory"]
    E["Quarantine or escalate"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 retry_orchestrator.py sample_failures.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
