import os
import pandas as pd
from tabulate import tabulate
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
res = []
headers = ["name", "difficult"]
for i, row in df.iterrows():
    res.append([row["verbose_name"].split(".")[0], row["difficult"]])
print(tabulate(res, tablefmt="pipe", floatfmt=".2f", headers = headers))
