import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "synthetic_demo.csv"

class SyntheticDataFormatTests(unittest.TestCase):
    def test_csv_exists_and_has_expected_columns(self):
        self.assertTrue(CSV_PATH.exists())
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.assertEqual(reader.fieldnames, ["time", "Fp1", "Fp2", "C3", "C4"])

    def test_rows_are_numeric_and_nonempty(self):
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertGreater(len(rows), 0)
        for row in rows:
            for key in ["time", "Fp1", "Fp2", "C3", "C4"]:
                self.assertTrue(row[key].strip())
                float(row[key])

    def test_demo_has_200_samples(self):
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 200)

if __name__ == "__main__":
    unittest.main()
