import tkinter as tk
from tkinter import filedialog
from pymatgen.core.surface import SlabGenerator
from pymatgen.core.structure import Structure
from ase.io import write
from pymatgen.io.ase import AseAtomsAdaptor
from ase.visualize import view


def generate_slab(contcar_path, miller_indices, min_slab_size, min_vacuum_size, lll_reduce, orthogonalize_c):
    try:
        structure = Structure.from_file(contcar_path)
    except Exception as e:
        raise ValueError(f"Failed to read Bulk file: {e}")

    try:
        slabgen = SlabGenerator(structure, miller_indices, min_slab_size, min_vacuum_size, lll_reduce)
        slab = slabgen.get_slab()
        if orthogonalize_c:
            slab = slab.get_orthogonal_c_slab()
    except Exception as e:
        raise RuntimeError(f"Failed to generate slab: {e}")

    return slab

def submit():
    contcar_path = contcar_entry.get()
    miller_indices = tuple(map(int, miller_entry.get().split()))
    min_slab_size = float(min_slab_entry.get())
    min_vacuum_size = float(min_vacuum_entry.get())
    lll_reduce = lll_reduce_var.get()
    orthogonalize_c = orthogonalize_c_var.get()

    try:
        slab = generate_slab(contcar_path, miller_indices, min_slab_size, min_vacuum_size, lll_reduce, orthogonalize_c)
        atoms = AseAtomsAdaptor.get_atoms(slab)
        output_filename = f"POSCAR{''.join(map(str, miller_indices))}.vasp"
        write(output_filename, atoms, format='vasp')
        print(f"Slab saved to {output_filename}")
        
        # Visualize the structure
        view(atoms)
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def browse_bulk():
    bulk_file = filedialog.askopenfilename()
    contcar_entry.insert(tk.END, bulk_file)

root = tk.Tk()
root.title("Slab creator GUI")

tk.Label(root, text="CONTCAR File Path:").grid(row=0, column=0)
tk.Label(root, text="Miller Indices (h k l):").grid(row=1, column=0)
tk.Label(root, text="Minimum Slab Size (Ang):").grid(row=2, column=0)
tk.Label(root, text="Minimum Vacuum Size (Ang):").grid(row=3, column=0)
tk.Label(root, text="LLL reduction:").grid(row=4, column=0)
tk.Label(root, text="Force c to be orthogonal to a and b:").grid(row=5, column=0)

contcar_entry = tk.Entry(root)
miller_entry = tk.Entry(root)
min_slab_entry = tk.Entry(root)
min_vacuum_entry = tk.Entry(root)
contcar_entry.grid(row=0, column=1)
miller_entry.grid(row=1, column=1)
min_slab_entry.grid(row=2, column=1)
min_vacuum_entry.grid(row=3, column=1)

bulk_button = tk.Button(root, text="Browse", command=browse_bulk)
bulk_button.grid(row=0, column=2)

lll_reduce_var = tk.BooleanVar()
lll_reduce_checkbox = tk.Checkbutton(root, variable=lll_reduce_var, onvalue=True, offvalue=False)
lll_reduce_checkbox.grid(row=4, column=1)

orthogonalize_c_var = tk.BooleanVar()
orthogonalize_c_checkbox = tk.Checkbutton(root, variable=orthogonalize_c_var, onvalue=True, offvalue=False)
orthogonalize_c_checkbox.grid(row=5, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2)

root.mainloop()

