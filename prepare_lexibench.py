import os
import shutil

d = "lexibench_bin_msas"
for ds in os.listdir(d):
    subd = os.path.join(d, ds)
    if not os.path.isdir(subd):
        continue
    oldp = os.path.join(subd, "bin.phy")
    newp = os.path.join(d, ds + ".phy")
    shutil.move(oldp, newp)
    shutil.rmtree(subd)
