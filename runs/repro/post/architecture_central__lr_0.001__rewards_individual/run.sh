#!/bin/bash
#
#SBATCH --workdir=.
#SBATCH --cores=6
#SBATCH --time 1:0:0
#SBATCH --mem 32GB
#SBATCH --output=runs/repro/post/architecture_central__lr_0.001__rewards_individual/log.log
#SBATCH --job-name=architecture_central__lr_0.001__rewards_individual
#SBATCH --partition quick
#!/bin/bash

module load python/3.7

source .venv/bin/activate

echo "Entered environment"

post runs/repro/post/architecture_central__lr_0.001__rewards_individual runs/repro/train/rewards_individual__architecture_central__lr_0.001
