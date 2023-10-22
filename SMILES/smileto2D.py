#!/bin/python3
from rdkit import Chem
from rdkit.Chem import Draw
import os
def smiles_to_image(smiles, output_file):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(800, 800))
    img.save(output_file)

DIRPATH=os.listdir('./molecules')
for smilepath in DIRPATH:
    path = "./molecules/"+smilepath

    with open(path,"r") as data:
        lines = data.readlines()

        #print(content)
        # Example usage
        j=0
        for i in lines:
            smiles = i
            j=j+1
            output_file = smilepath+"molecule"+str(j)+".png"  # Replace with your desired output file name
            print("\n")
            print("output_file is :",output_file)
            print("smiles is :",smiles)
            print("\n")
            smiles_to_image(smiles,'generated_structures/'+output_file)
            '''
            try:
                smiles_to_image(smiles,'generated_structures/'+output_file)
            except:
                "Failed to convert file into image. Check if pillow is installed."
                pass
            '''
