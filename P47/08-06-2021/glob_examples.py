import glob

# Show paths

paths = glob.glob("./*", recursive=True)
print(paths)

for path in glob.iglob("./*", recursive=True):
    print(path)
