import os
import shutil

d = "babelnet_bin_msas"
for group in os.listdir(d):
    subd = os.path.join(d, group)
    if not os.path.isdir(subd):
        continue
    for msa in os.listdir(subd):
        oldp = os.path.join(subd, msa)
        newp = os.path.join(d, group + "_" + msa)
        shutil.move(oldp, newp)
