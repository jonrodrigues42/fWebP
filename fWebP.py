# converts WebP to PNG 
# created by Jon Rodrigues
# https://github.com/jonrodrigues42


# To-do:
## better way to found the path (just change de chdir?)
## use tqdm to show a progress bar
### translate to Portuguese?
### check if the file existis before starting

import glob, os, sys, time
from PIL import Image
from tqdm import tqdm

# the main funcion of the program
def convert(source, dest):
    with Image.open(source) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(dest, "PNG")

# constants
PATH = "images"
SUBFOLDER = "converted"
os.chdir(PATH)

# variables
paths = glob.glob("*webp")
cwd = os.getcwd() # current working dir


if len(paths) == 1:
    print(f"\nFound {len(paths)} file, iniating the process.\n")    # singular 
elif len(paths) > 1:
    print(f"\nFound {len(paths)} files, iniating the process.\n")   # plural
else:
    print("No .WebP was found. Exiting now")    # no file
    sys.exit()

print("Beware: If a file already exists, it will be overwritten!")
print("Ctrl+C to cancel the process\n")    


# Wait 3 seconds after the above warning, printing the remaining time
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("\n\n")

# Check if the folder "converted"  already existis, if not, creates the folder"
if not os.path.exists(SUBFOLDER):
    os.mkdir(os.path.join(cwd, SUBFOLDER))

# # Calls the function
# for path in paths:
#     print(f"Found '{path}', converting to PNG.")
#     convert(path, subfolder + "\\" + path[:-5] + ".png")

# define the progressbar size
chunk_size = 100/len(paths)

# loop through the files and convert them
for path in tqdm(paths, desc="Converting files", unit="file", ncols=80):
    output_file = os.path.join(SUBFOLDER, os.path.splitext(path)[0] + ".png")
    convert(path, output_file)

# Finishes the process
print("\n\nProcess finished.\n")
sys.exit()