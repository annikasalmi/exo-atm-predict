# Exoplanet Atmosphere Predictor

A data analysis project that predicts atmospheric characteristics of exoplanets based on existing observational data. This tool combines multiple astronomical datasets to model and predict atmospheric properties for planets where direct observations are limited or unavailable.

## Overview

The goal of this project is to enable researchers and enthusiasts to select any exoplanet and receive predictions about its most likely atmospheric characteristics. The predictions are based on patterns learned from confirmed atmospheric observations, making it a valuable tool for prioritizing future observations and understanding planetary formation.

## Features

- **Data Integration**: Combines NASA's Exoplanet Archive with the Canary Islands Exoatmospheres Table
- **Atmospheric Prediction**: Predicts atmospheric composition, temperature, and other key characteristics
- **Interactive Selection**: Choose specific exoplanets by name or randomly select from the database
- **Transparency**: Clearly distinguishes between observed data and model predictions
- **Visualization Tools**: (Planned) Interactive plotting and visualization capabilities

## Data Sources

This project integrates data from multiple authoritative sources:

- **[NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)**: Comprehensive database of confirmed exoplanets
  - Uses PSCompPars dataset (one row per planet for consistency)
- **[Canary Islands Exoatmospheres Table](https://research.iac.es/proyecto/exoatmospheres/table.php)**: Detailed atmospheric observations and measurements
- **[PICASO](https://github.com/natashabatalha/picaso)**: Planetary atmospheric modeling framework for temperature and composition calculations

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/exo-atm-predict.git
cd exo-atm-predict
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
exo-atm-predict/
├── data/                                    # Data files
│   ├── iac_exoplanet_atmospheres-2024.csv  # Canary Islands atmospheric data
│   └── PSCompPars_2024.09.11_03.30.09.csv  # NASA exoplanet data
├── data_ingestion.py                        # Data processing and combination
├── requirements.txt                         # Python dependencies
└── README.md                               # This file
```

## How It Works

1. **Data Integration**: The NASA Exoplanet database and Canary Islands Exoatmospheres Table are combined and cleaned
2. **Planet Selection**: Users can either:
   - Type in the name of a specific exoplanet
   - Randomly select one from the database
3. **Atmospheric Modeling**: The selected exoplanet becomes an `Exoplanet` class instance with:
   - Observed properties from existing data
   - Predicted atmospheric characteristics based on similar planets
   - Temperature calculations using PICASO framework
4. **Exploration**: Users can explore both real observations and model predictions, with clear distinction between the two

## Current Status

**Work in Progress** - This project is actively under development. Current capabilities include:

- ✅ Data ingestion and cleaning pipeline
- ✅ Basic data combination from multiple sources
- 🔄 Exoplanet class implementation
- 🔄 Atmospheric prediction algorithms
- 🔄 Interactive selection interface
- 📋 Visualization tools (planned)

## Usage

Currently, the main functionality is in the data ingestion phase. To run the data processing:

```python
python data_ingestion.py
```

This will:
- Load and clean the atmospheric and exoplanet datasets
- Remove controversial or unconfirmed planets
- Combine the datasets based on planet and star names
- Prepare the data for atmospheric modeling

## Future Development

- **Machine Learning Models**: Implement predictive algorithms for atmospheric characteristics
- **Interactive Interface**: Web-based or CLI tool for planet selection and exploration
- **Advanced Visualizations**: 3D atmospheric models, comparison plots, and statistical analyses
- **Real-time Updates**: Integration with live astronomical databases
- **API Development**: RESTful API for programmatic access

## Contributing

This project is open to contributions! Areas where help is especially welcome:

- Atmospheric modeling algorithms
- Data visualization tools
- Machine learning model development
- Documentation and testing
- Performance optimization

## License

MIT License

## Acknowledgments

- NASA Exoplanet Archive team for maintaining comprehensive exoplanet data
- Instituto de Astrofísica de Canarias for atmospheric observations database
- PICASO development team for atmospheric modeling tools
- The broader exoplanet research community for observational data

## 📞 Contact

[Add your contact information here]

---

*This project aims to bridge the gap between observed exoplanet atmospheres and the vast number of planets where atmospheric data is limited, helping prioritize future observations and advance our understanding of planetary formation and evolution.*

