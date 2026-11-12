# Ml Training Retry Orchestrator architecture

Classifies failed ML training jobs into retry, quarantine, or escalate actions based on failure mode and recent retry history.

```mermaid
flowchart LR
    N0["sample_failures.csv"]
    N1["retry_orchestrator.py"]
    N2["next action / actions"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
