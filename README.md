# AI / CI

This repository contains all code to reproduce the results of the study
"Adversarial dynamics in human-machine systems" by Levin Brinkmann, Manuel
Cebrian, and Niccolò Pescetelli.


## Setup

These scripts have been tested with python 3.7.

The following commants

* create a new virtual environment
* update pip and install wheel
* install the main package (aci) and all its requirements
* install the djx package for parallelisation on slurm cluster

```
python3.7 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install -e ".[dev]"
pip install -e djx
```

## Reproduce visualisations in the manuscript

### Lineplots with different metrics (coordination, predictions, entropy, ...)

```
notebooks/plot_metrics.ipynb
```

### Visualisations of individual episodes (color matrix)

```
notebooks/plot_colors.ipynb
```

## Run on a Slurm cluster

This repository contains scripts that allows to run the simulation on slurm
clusters. See below to reproduce an individual simulation locally.

First adapt the corresponding job pattern to the settings needed for your cluster:
djx/djx/job_pattern/gpu.sh

### Train

Run the multi-agent Q-learning simulation. This is creating a grid of different
settings. A single independent slrum job is created for each point in the grid.

```
djx train runs/repro
```

### Postprocess

Postprocess the traces collected during training. Here we compute metrics such
as entropy and Jensen-Shannon divergence.

```
djx post runs/repro
```

### Merge

Merge the post-processed files of the different runs.

```
merge runs/repro
```

## Local reproduction

The following is for an AI with a central (global) architecture and a learning
rate of 0.001.

### Train

```
train runs/repro/train/rewards_individual__architecture_central__lr_0.001
```

### Postprocess

```
post runs/repro/post/architecture_central__lr_0.001__rewards_individual runs/repro/train/rewards_individual__architecture_central__lr_0.001
```

