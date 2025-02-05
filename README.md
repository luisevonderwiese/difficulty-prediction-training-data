# Ground Truth Difficulties for Language Data
This is a fork of the [Difficulty Prediction Training Data Pipeline](https://github.com/tschuelia/difficulty-prediction-training-data) to compute ground truth difficulties on language data.
Here we provide instructions for obtaining ground truth difficulties for data from different sources.
* MSAs constructed for the datasets in [lexibench](https://github.com/lexibank/lexibench)
* MSAs extracted automatically from [BabelNet](https://babelnet.org/) ([main experiment](https://github.com/luisevonderwiese/babel2msa))
* MSAs resulting from a reverse-engineering study on dara from [NorthEuralex](http://northeuralex.org/) ([main experiment](https://github.com/luisevonderwiese/babel2msa))

### Installation
1. Clone this repo: 
```
git clone https://github.com/luisevonderwiese/difficulty-prediction-training-data.git`
cd difficulty-prediction-training-data
git checkout tree_characterization
```
2. Install RAxML-NG by following the instructions in [the GitHub repo](https://github.com/amkozlov/raxml-ng).
3. Install IQ-Tree by following the instructions on [their website](http://www.iqtree.org).
4. Setup the conda environment:
    ```
    conda env create -f environment.yml
    ```
   Tipp: use mamba for faster dependency solving. You can simply install mamba by running `conda install mamba -c conda-forge` and then replace `conda` in this command with `mamba`.
5. Activate the new conda environment:
   ```
   conda activate difficulty
   ```
6. Install the required R-Package RPANDAS by running `python install_rpanda.py`. This might take a few minutes to finish. Please check the output of this script for any errors. 
Installing R packages from python can be a bit messy. If it complains that some R package, e.g. `randomPackage` is missing, try installing it using mamba and conda-forge and adding the prefix `r-`: `mamba install r-randomPackage -c conda-forge`  If there is any issue feel free to contact me.

#### System Requirements
The pipeline in this state currently only works on x86 unix machines. It does especially not run on OSX-ARM machines. 
This is due to missing cross-compilations of required R packages in conda-forge.


### Setting up the input data

#### lexibench
* From [lexibench repo](https://github.com/lexibank/lexibench) copy `generated_data/msa/` into `lexibench_bin_msas/`
* Run `python prepare_lexibench.py`

#### babelnet
* From [main experiment repo](https://github.com/luisevonderwiese/babel2msa) copy: 
	* `results/all/msa/` into `babelnet_bin_msas/all`
	* `results/dense/msa/` into `babelnet_bin_msas/dense`
	* `results/iecor/msa/` into `babelnet_bin_msas/iecor`
* Run `python prepare_babelnet.py`

#### northeuralex
* From [main experiment repo](https://github.com/luisevonderwiese/babel2msa) copy `results/northeuralex/msa/` into `northeuralex_bin_msas`

### Running the pipeline
1. Use the right config file:
	* lexibench: `cp config_lexibench.yaml config.yaml`
	* babelnet: `cp config_babelnet.yaml config.yaml` 
	* northeuralex: `cp config_northeuralex.yaml config.yaml`
2. Check the `config.yaml` file:
   * In the `software` section provide the paths to executables of RAxML-NG, IQ-Tree from the above installs.
3. Run `snakemake -n --quiet` for a dry run of snakemake. Snakemake will print a summary of all tasks it will execute to the console.
4. Finally, start the pipeline with `snakemake --cores [num_cores]`.    
If you intend to run snakemake on a slurm cluster, you might want to check out [my instructions](https://github.com/tschuelia/snakemake-on-slurm-clusters) on how to set up snakemake for slurm.



### Collecting data and printing ground truth difficulties

#### lexibench
```
python final_data_collection.py --dir results_lexibench
python print_difficult.py --dir results_lexibench
```

#### babelnet
```
python final_data_collection.py --dir results_babelnet
python print_difficult.py --dir results_babelnet
```

#### northeuralex
```
python final_data_collection.py --dir results_northeuralex
python print_difficult.py --dir results_northeuralex
```

