This repository contains the raw data and analysis that are the supporting information to the [`bletl`](https://github.com/jubiotech/bletl) paper.

# Contents
The unprocessed raw data was placed in the `data` directory.

The `notebooks` directory contains Jupyter notebooks for all analyses and figures in the manuscript.

Figures were not `git`-committed, but the extracted time series features and t-SNE were exported to the `results` folder.

# Installation
While the `bletl` package itself may be [installed from PyPI](https://github.com/JuBiotech/bletl#installation), this repository with the full analysis also depends on [PyMC3](https://github.com/pymc-devs/pymc3) that can be a little tricky to install.
For this reason we provide an `environment.yml` file that can be used to reproduce a Python environment with all the dependencies:

```
conda env create -f environment.yml
```

The new environment is named `bletl_env` and can be activated with `conda activate bletl_env`.

After that a Jupyter notebook server can be launched with `jupyter notebook`.

# References
* [`bletl` source code](https://github.com/JuBiotech/bletl)
* [`bletl` documentation](https://bletl.readthedocs.io)
