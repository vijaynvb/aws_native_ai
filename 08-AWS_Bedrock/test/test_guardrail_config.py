import importlib.util
import os
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "01-basicmodel.py"


def load_module():
    spec = importlib.util.spec_from_file_location("bedrock_basic_model", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GuardrailConfigTests(unittest.TestCase):
    def test_build_invoke_params_includes_guardrail_config(self):
        os.environ["BEDROCK_GUARDRAIL_ID"] = "gr-123"
        os.environ["BEDROCK_GUARDRAIL_VERSION"] = "DRAFT"
        os.environ["BEDROCK_GUARDRAIL_TRACE"] = "ENABLED"

        module = load_module()
        params = module.build_invoke_params({"messages": []}, "demo-model")

        self.assertEqual(params["guardrailIdentifier"], "gr-123")
        self.assertEqual(params["guardrailVersion"], "DRAFT")
        self.assertEqual(params["trace"], "ENABLED")

    def test_build_invoke_params_skips_guardrail_when_not_configured(self):
        os.environ.pop("BEDROCK_GUARDRAIL_ID", None)
        os.environ.pop("BEDROCK_GUARDRAIL_VERSION", None)

        module = load_module()
        params = module.build_invoke_params({"messages": []}, "demo-model")

        self.assertNotIn("guardrailIdentifier", params)
        self.assertNotIn("guardrailVersion", params)
        self.assertNotIn("trace", params)


if __name__ == "__main__":
    unittest.main()
