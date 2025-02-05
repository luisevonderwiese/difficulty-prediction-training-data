import os
import shutil
from padd_msa import padd_msa


d = "lexibench_bin_msas"
for ds in os.listdir(d):
    subd = os.path.join(d, ds)
    if not os.path.isdir(subd):
        continue
    oldp = os.path.join(subd, "bin.phy")
    newp = os.path.join(d, ds + ".phy")
    shutil.move(oldp, newp)
    shutil.rmtree(subd)
    try:
        AlignIO.read(newp)
    except:
        padd_msa(newp)
