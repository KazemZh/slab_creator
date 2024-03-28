from pymatgen.core.surface import SlabGenerator
from pymatgen.core.structure import Structure

# Read the CONTCAR file
contcar_path = "CONTCAR-bulk"
structure = Structure.from_file(contcar_path)

# Define the Miller indices for the slab orientation
miller_indices = (0, 1, 2)

# Create a SlabGenerator object
slabgen = SlabGenerator(structure, miller_indices, 10, 10, lll_reduce=True)  # Adjust sizes as needed

# Generate the slab
slab = slabgen.get_slab()
slab = slab.get_orthogonal_c_slab() # force c to be perpendicular to a and b cell vectors

# Print the slab information
print("Slab structure:")
slab.to("POSCAR_slab.vasp")
print(slab)
