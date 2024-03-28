Usage
=====

To use the script, follow these steps:

1. Launch the script by running the slab_creator.py file.
2. Provide the path to the CONTCAR file containing the bulk structure.
3. Enter the Miller indices for the desired slab orientation.
4. Specify the minimum slab size and minimum vacuum size in Angstroms.
5. Choose whether to apply LLL reduction (orthogonalize) to the slab.
6. Choose whether to force the slab to be perpendicular to the c-axis.

The generated slab will be saved in VASP format with the specified Miller indices in the filename (e.g., POSCAR100.vasp). Additionally, the script will visualize the slab structure using the ASE package in the gui version of the code.
