import os
from Bio import AlignIO

def padd_msa(msa_path):
    with open(msa_path, "r") as msa_file:
        msa_string = msa_file.read()
    parts = msa_string.split("\n\n")
    lines = parts[-1].split("\n")
    block_size = len(lines[1].split(" ")[-1])
    if block_size == 10:
        padding_size = 10
        append_string = " ----------"
    else:
        padding_size = 10 - block_size
        append_string = "-" * padding_size
    if len(parts) != 1:
        msa_string = "\n\n".join(parts[:-1] + ["\n".join([line + append_string for line in lines[:-1]] + [lines[-1]])])
    else:
        msa_string = "\n".join([lines[0]] + [line + append_string for line in lines[1:-1]] + [lines[-1]])

    parts = msa_string.split("\n")
    sub_parts = parts[0].split(" ")

    msa_string = "\n".join([" ".join(sub_parts[:-1] + [str(int(sub_parts[-1]) + padding_size)])] + parts[1:])

    with open(msa_path, "w+") as new_msa_file:
        new_msa_file.write(msa_string)
