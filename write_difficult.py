import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--dir",
    type=str,
    required=True,
    help="Results directory to look for parquet files.",
)

args = parser.parse_args()

df = pd.read_parquet(os.path.join(args.dir, 'all_data.parquet'))

out_dir = "ground_truth_difficulties"
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)
out_path = os.path.join(out_dir, args.dir.split("/")[0] + "_difficult.csv")
with open(out_path, "w+") as outfile:
    outfile.write("dataset,difficult\n")
    for i, row in df.iterrows():
        outfile.write(row["verbose_name"].split(".")[0] + "," + str(row["difficult"]) + "\n")
