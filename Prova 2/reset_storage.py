# Delete PKL files

import os

files_to_create = ["app/storage/usuarios.pkl"]
for file in os.listdir():
    if file.endswith(".pkl"):
        os.remove(file)

# Create files
for file in files_to_create:
    f = open(file, "w")

