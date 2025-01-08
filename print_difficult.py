import os
import pandas as pd
from tabulate import tabulate

results_dir = "results_northeuralex"
df = pd.read_parquet(os.path.join(results_dir, 'all_data.parquet'))
res = []
headers = ["name", "difficult"]
for i, row in df.iterrows():
    res.append([row["verbose_name"].split(".")[0], row["difficult"]])

print(tabulate(res, tablefmt="pipe", floatfmt=".2f", headers = headers))
