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
