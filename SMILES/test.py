#!/bin/python3
from rdkit import Chem
from rdkit.Chem import Draw
import os
def smiles_to_image(smiles, output_file):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(300, 300))
    img.save(output_file)
path = "./molecules/Output"

with open(path,"r") as data:
    lines = data.readlines()
#print(content)
# Example usage
j=0
for i in lines:
    smiles = str(i)
    print(smiles)
    j=j+1
    output_file = "molecule"+str(j)+".png"  # Replace with your desired output file name

    smiles_to_image(smiles, output_file)

