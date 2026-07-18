import unittest

from retry_orchestrator import actions, next_action


class RetryOrchestratorTest(unittest.TestCase):
    def test_retries_spot_interruption_under_limit(self):
        row = {"error_type": "spot_interruption", "retries": "1"}
        self.assertEqual(next_action(row), "retry")

    def test_quarantines_data_contract_failure(self):
        row = {"error_type": "data_contract", "retries": "0"}
        self.assertEqual(next_action(row), "quarantine")

    def test_formats_actions(self):
        rows = [{"run_id": "r1", "pipeline": "p", "error_type": "oom", "retries": "4"}]
        self.assertEqual(actions(rows)[0]["action"], "escalate")


if __name__ == "__main__":
    unittest.main()
