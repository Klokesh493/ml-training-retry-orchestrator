# Ml Training Retry Orchestrator architecture

Classifies failed ML training jobs into retry, quarantine, or escalate actions based on failure mode and recent retry history.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
