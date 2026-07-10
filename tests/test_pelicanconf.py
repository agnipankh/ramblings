from pathlib import Path
import unittest

import pelicanconf


class PelicanConfigurationTest(unittest.TestCase):
    def test_theme_resolves_to_the_checked_out_theme(self):
        expected_theme = Path(__file__).resolve().parents[1] / "themes" / "attila"

        self.assertEqual(Path(pelicanconf.THEME).resolve(), expected_theme)


if __name__ == "__main__":
    unittest.main()
