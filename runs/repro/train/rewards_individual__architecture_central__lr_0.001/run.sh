#!/bin/bash -l
#
#SBATCH --workdir=.
#SBATCH --cores=2
#SBATCH --output=runs/repro/train/rewards_individual__architecture_central__lr_0.001/log.log
#SBATCH --job-name=rewards_individual__architecture_central__lr_0.001
#SBATCH --gres=gpu
#SBATCH --partition gpu

set -e

module load python/3.7
module load cuda

source .venv/bin/activate

echo "Entered environment"

train runs/repro/train/rewards_individual__architecture_central__lr_0.001
