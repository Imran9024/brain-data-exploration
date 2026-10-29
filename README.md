# Interactive Visual Analytics for Brain Data Exploration

A B.Tech Phase-II project prototype for exploring multi-channel brain-signal data through an interactive browser dashboard.

> **Project status:** Academic prototype / Phase-II planning and implementation. The bundled CSV contains **synthetic demonstration data**. This repository does not claim clinical validity and has not been validated for diagnosis or patient care.

## Project overview

The project aims to make brain-data exploration more accessible by combining data loading, channel selection, filtering, visual inspection, descriptive statistics, and basic channel-to-channel correlation in one interface.

### Objectives
- Load and inspect structured signal data from a CSV file.
- Select channels and adjust the visible sample range.
- Visualize multi-channel signals interactively.
- Calculate simple descriptive statistics.
- Explore pairwise correlation between selected channels.
- Provide an understandable workflow for students and researchers.

## Repository structure

```text
brain-data-exploration/
├── app/
│   └── index.html                 # Browser dashboard (self-contained)
├── assets/
│   └── architecture.svg           # System architecture diagram
├── data/
│   └── synthetic_demo.csv         # Example data; not real patient data
├── docs/
│   ├── Phase_II_Project_Presentation.pptx
│   ├── Phase_II_Technical_Report.docx
│   ├── ARCHITECTURE.md
│   ├── TESTING.md
│   └── PROJECT_PLAN.md
├── screenshots/                   # Add genuine screenshots after running the app
├── src/
│   └── README.md                  # Notes for future modular implementation
├── tests/
│   └── test_data_format.py        # Basic CSV-format checks
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Features in the current prototype

- **CSV upload:** load a local CSV containing a sample/time column and numeric signal channels.
- **Channel selection:** choose which channels are shown.
- **Sample-window control:** adjust the portion of the data being viewed.
- **Signal chart:** render selected channels using the browser's Canvas API.
- **Summary statistics:** sample count, mean, minimum, maximum and standard deviation.
- **Correlation heatmap:** calculate pairwise Pearson correlations for selected channels.
- **Data preview:** inspect a small table of rows.
- **CSV export:** export the currently selected window.

The dashboard uses plain HTML, CSS and JavaScript. It does not require a package installation or an external charting library to render the included demonstration.

## Run locally

1. Download or clone this repository.
2. Open `app/index.html` in a modern browser (Chrome, Edge, Firefox or Safari).
3. The synthetic sample data loads automatically.
4. Use **Load CSV** to select a local CSV file.

No server or Python environment is required for the current static prototype.

## CSV format

- One row per time/sample point.
- The first column may be named `time`, `timestamp`, `sample`, or `index`.
- Remaining columns should contain numeric channel values, for example `Fp1`, `Fp2`, `C3`, `C4`.
- Missing/non-numeric values are skipped in calculations where possible.

Example:

```csv
time,Fp1,Fp2,C3
0,0.21,0.12,-0.05
1,0.35,0.18,0.02
2,0.11,0.08,0.13
```

## Testing

See [`docs/TESTING.md`](docs/TESTING.md). Run the CSV format checks with:

```bash
python -m unittest discover -s tests -v
```

The automated test currently validates the bundled CSV structure. Browser interactions should also be checked manually and recorded in the testing document. Do not report test outcomes that have not actually been observed.

## Architecture and project plan

- [System architecture](docs/ARCHITECTURE.md)
- [Project plan and milestones](docs/PROJECT_PLAN.md)
- [Testing plan](docs/TESTING.md)
- [Technical report](docs/Phase_II_Technical_Report.docx)
- [Presentation](docs/Phase_II_Project_Presentation.pptx)

## Limitations and responsible use

- Bundled data is synthetic and intended only to demonstrate UI behaviour.
- The prototype is not a medical device and must not be used to make clinical decisions.
- EEG-style channels in the sample are illustrative; they are not recorded from a person.
- The current version focuses on time-series CSV data. MRI/fMRI/MEG/DTI image and volume workflows are future work.
- Results depend on the quality, units, sampling rate and preprocessing of any supplied dataset.

## Academic metadata

- **Project:** Interactive Visual Analytics for Brain Data Exploration
- **Programme:** B.Tech, Computer Science & Engineering
- **Institution:** IILM University, Greater Noida
- **Academic session:** 2026–27
- **Phase:** Phase II

> Before submission, verify the team/guide metadata with your official project records and add real screenshots from the running prototype.
