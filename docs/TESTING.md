# Testing Plan and Evidence Log

**Important:** This document is a plan, not a claim that all tests have passed. Enter observed outcomes only after executing each test on the target computer.

| ID | Test | Steps | Expected result | Observed result |
|---|---|---|---|---|
| T01 | Initial load | Open `app/index.html` in a modern browser | Dashboard and demo signals appear | To be recorded |
| T02 | Channel toggling | Uncheck and re-check a channel | Chart/statistics/heatmap update | To be recorded |
| T03 | Sample range | Move start/end sliders | Visible sample count and plots update | To be recorded |
| T04 | Display mode | Choose centered or z-score mode | Signal chart rescales | To be recorded |
| T05 | Valid CSV | Upload `data/synthetic_demo.csv` | File loads and channel list appears | To be recorded |
| T06 | Invalid CSV | Upload a file with one column or no data rows | Clear CSV error message | To be recorded |
| T07 | Export | Select channels/window and click Export | CSV downloads with selected columns/window | To be recorded |
| T08 | Responsive layout | Resize browser to mobile width | Controls and panels stack without overlap | To be recorded |
| T09 | Statistics sanity check | Compare a small hand-calculated dataset with displayed values | Calculations match expected values | To be recorded |
| T10 | Research dataset | Load a suitably licensed, documented research CSV | Data loads; limitations/units are documented | Not yet performed |

## Data and ethics checklist
- Record the source, licence, download date and citation for any real research dataset.
- Prefer public, appropriately licensed and de-identified data.
- Do not upload identifiable health information.
- Record sampling frequency, units, preprocessing and missing-value handling.
- Do not interpret correlations as causation or as medical findings.
- Capture screenshots only from actual runs and label the dataset used.

## CSV format unit check
Run:

```bash
python -m unittest discover -s tests -v
```
