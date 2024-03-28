# Slab Generator

Slab Generator is a Python script that generates slab structures from a given structure file (CONTCAR) using the pymatgen package.

## Installation

Before using Slab Generator, make sure you have the pymatgen package installed. You can install it using pip:

pip install pymatgen


## Usage

To generate a slab structure, run the `slab_creator.py` script and follow the prompts:

python slab_creator.py

You will be prompted to provide the path to the input file (e.g., CONTCAR-bulk), Miller indices for the slab orientation, minimum slab size, minimum vacuum size, and whether to apply LLL reduction (orthogonalize) to the slab.

After providing the required inputs, the script will generate the slab structure and save it to a VASP POSCAR file.

Or you can run the GUI version of the code in the gui directory:

python slab_creator+gui.py

then fill the required variables.

## Example

Here's an example of using Slab Generator:

1. Run the script: python slab_generator.py
2. Enter the path to the input file: `CONTCAR-bulk`
3. Enter the Miller indices for the slab orientation: `1 0 0`
4. Enter the minimum slab size: `10`
5. Enter the minimum vacuum size: `15`
6. Do you want to apply LLL reduction (orthogonalize) to the slab? (True/False): `True`

The script will generate the slab structure and save it to a file named `POSCAR100.vasp`.

