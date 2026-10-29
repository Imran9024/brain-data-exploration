# Brain Data Explorer — Phase II Prototype

## What is included
- `index.html`: self-contained browser UI (Plotly is loaded from a CDN)
- `synthetic_demo.csv`: generated synthetic multi-channel signal sample
- `Phase_II_Technical_Report.docx`: project report
- `Phase_II_Project_Presentation.pptx`: presentation

## Run
1. Extract the ZIP.
2. Open `index.html` in a modern browser with internet access.
3. Try the built-in sample, or upload a CSV with a `time` column and one or more numeric signal columns.
4. Select a channel and adjust the time range; inspect the signal plot, summary statistics, heatmap and preview.
5. Use Download loaded CSV to export the loaded rows.

## Important limitations
- Built-in signals are synthetic and are only for demonstrating interface behavior.
- The prototype has not been validated on real EEG/MRI/fMRI/MEG data.
- No clinical or diagnostic claims are supported.
- Run the test cases in the report and record actual outcomes before submitting results as completed validation.
