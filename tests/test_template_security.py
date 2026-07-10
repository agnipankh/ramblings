from pathlib import Path
import unittest


class TemplateSecurityTest(unittest.TestCase):
    def test_templates_do_not_reference_compromised_polyfill_domain(self):
        theme_root = Path(__file__).resolve().parents[1] / "themes" / "attila"
        templates = theme_root.glob("templates/**/*.html")
        blocked_domain = "polyfill" + "." + "io"

        references = [
            str(template)
            for template in templates
            if blocked_domain in template.read_text(encoding="utf-8").lower()
        ]

        self.assertEqual(references, [])


if __name__ == "__main__":
    unittest.main()
