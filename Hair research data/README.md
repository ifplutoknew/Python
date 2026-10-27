# Dry Hair Tensile Research Data

This folder contains tensile test data and Jupyter notebooks for exploring the stress–strain behavior of dry curly and straight hair samples at different extension rates. The notebooks visualize the measurements, summarize repeated strain values, and fit models to examine the toe and elastic regions of the stress–strain response.

## Folder contents

### Analysis notebooks

- `Dry curly hair_2mm.ipynb`, `Dry curly hair_20mm.ipynb`, `Dry curly hair_200mm.ipynb`, and `Dry curly hair_2000mm.ipynb` analyze curly-hair samples.
- `Dry straight_2mm.ipynb`, `dry straight_20mm.ipynb`, `Dry straight hair_200mm.ipynb`, and `Dry straight hair_2000mm.ipynb` analyze straight-hair samples.
- `Analysis graphs.ipynb` plots summary measurements, including toe length, effective toe stiffness, and transition stress, across strain rates.

The rate in each notebook's filename is the extension rate in millimeters per minute (mm/min).

### Data

- `dry curly hair data/` contains CSV datasets for curly-hair measurements.
- `dry straight hair data/` contains CSV datasets for straight-hair measurements.
- `Dry Hair samples text file/` contains tensile-instrument text exports for the available samples.

The CSV datasets use these columns:

| Column | Description |
|---|---|
| `Record` | Measurement record number |
| `Strain (%)` | Strain measurement, expressed as a percentage |
| `Stress (MPa)` | Stress measurement, in megapascals |

The text exports include instrument-report metadata before their tabular measurement data. They are source data; the analysis notebooks load the CSV files.

## Requirements

- Python 3
- Jupyter Notebook or JupyterLab
- `pandas`, `numpy`, `matplotlib`, and `scipy`

Install the Python packages with:

```bash
python -m pip install pandas numpy matplotlib scipy jupyter
```

## Running the notebooks

Open a terminal in this folder, start Jupyter, and open the notebook you want to run:

```bash
jupyter notebook
```

The analysis notebooks refer to CSV files using paths such as `dry curly hair data/...`. Run them with this folder as the working directory so those relative paths resolve correctly. Run the cells from top to bottom to load the data, generate plots and summaries, and fit the models.

## Notes

- The datasets are not uniform in which sample types and strain rates are available. Check the filenames before comparing groups.
- Filenames reflect the current files and are not perfectly consistent in capitalization or naming. In particular, the curly-hair 20 mm/min notebook loads `dry curly hair data/Extension_Dry_1_20mmmin_C.csv`.
- Some notebooks clean or convert values during analysis (for example, converting strain and stress to numbers and excluding invalid rows). The resulting plots and fits therefore depend on those notebook steps.
- Treat fitted parameters and comparisons as analysis results for these supplied measurements; inspect the notebook assumptions and data before drawing broader conclusions.
