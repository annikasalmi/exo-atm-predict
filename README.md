# exo-atm-predict
WORK IN PROCESS!

The goal is to be able to select any given exoplanet and it will tell you what the most "likely" characteristics of its atmosphere will be. This is obviously biased towards what we have already observed.

How it works (will work, as this is still a WIP):
1. The NASA Exoplanet database and the Canary Islands Exoatmospheres Table are combined. The data is cleaned
2. The user can either type in the name of an exoplanet or randomly select one
3. That exoplanet becomes its own class, Exoplanet. Based on the data that already exists for that planet and the other datasets, the attributes are filled in
4. Other attributes of the atmosphere are added like temperature, based on this dataset: https://github.com/natashabatalha/picaso/tree/master
5. The user can then explore this modeled, "average" attributes. It will be clear what is generated and what is real
6. I also want to add some cool plotting/viz tools - tbd

Mostly a repo for me to play with what the "average" exoplanet atmosphere based on the data we have.

Sources:
- Canary Islands Exoatmospheres Table: https://research.iac.es/proyecto/exoatmospheres/table.php
- NASA exoplanets dataset: https://www.kaggle.com/datasets/shivamb/all-exoplanets-dataset?resource=download
- PICASO: https://github.com/natashabatalha/picaso/tree/master

