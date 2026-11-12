# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 retry_orchestrator.py sample_failures.csv
tr-101: retry recsys-training
tr-102: quarantine vision-training
tr-103: escalate ranking-training
test_formats_actions (test_retry_orchestrator.RetryOrchestratorTest) ... ok
test_quarantines_data_contract_failure (test_retry_orchestrator.RetryOrchestratorTest) ... ok
test_retries_spot_interruption_under_limit (test_retry_orchestrator.RetryOrchestratorTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
````
