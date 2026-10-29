# Future modular source layout

The current prototype is intentionally self-contained in `app/index.html` to make the demo easy to run. If the project grows, split it into:
- `src/csv-loader.js` — parsing and validation
- `src/statistics.js` — descriptive statistics and correlation
- `src/visualization.js` — chart rendering
- `src/ui.js` — state and event wiring

This folder is a planning note, not a claim that these separate modules already exist.
