from pymatgen.core.surface import SlabGenerator
from pymatgen.core.structure import Structure

def generate_slab(contcar_path, miller_indices, min_slab_size, min_vacuum_size, lll_reduce, orthogonalize_c):
    """
    Generate a slab structure from a given structure file (CONTCAR).

    Args:
        contcar_path (str): Path to the CONTCAR file.
        miller_indices (tuple): Miller indices for the slab orientation.
        min_slab_size (int): Minimum slab size in Ang.
        min_vacuum_size (int): Minimum vacuum size in Ang.
        lll_reduce (bool): Whether to apply LLL reduction (orthogonalize) to the slab.
        orthogonalize_c (bool): Whether to force c to be perpendicular to a and b cell vectors.

    Returns:
        slab (Structure): Generated slab structure.
    """
    try:
        structure = Structure.from_file(contcar_path)
    except Exception as e:
        raise ValueError(f"Failed to read CONTCAR file: {e}")

    try:
        slabgen = SlabGenerator(structure, miller_indices, min_slab_size, min_vacuum_size, lll_reduce)
        slab = slabgen.get_slab()
        if orthogonalize_c:
            slab = slab.get_orthogonal_c_slab()
    except Exception as e:
        raise RuntimeError(f"Failed to generate slab: {e}")

    return slab

def main():
    try:
        contcar_path = input("Enter the path to the input file (e.g., CONTCAR-bulk): ")
        miller_indices = input("Enter the Miller indices for the slab orientation (e.g., 1 0 0): ").split()
        miller_indices = tuple(map(int, miller_indices))
        min_slab_size = int(input("Enter the minimum slab size in Ang: "))
        min_vacuum_size = int(input("Enter the minimum vacuum size in Ang: "))
        lll_reduce = input("Do you want to apply LLL reduction to the slab? (True/False): ").lower() == "true"
        orthogonalize_c = input("Do you want to force c to be perpendicular to a and b cell vectors? (True/False): ").lower() == "true"
        
        slab = generate_slab(contcar_path, miller_indices, min_slab_size, min_vacuum_size, lll_reduce, orthogonalize_c)
        output_filename = f"POSCAR{''.join(map(str, miller_indices))}.vasp"
        print("Slab structure:")
        print(slab)
        slab.to(output_filename)
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

