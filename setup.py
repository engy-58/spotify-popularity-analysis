import os

project_dir = os.getcwd()
subdirs = ['data/raw_data', 'data/processed_data', 'notebooks']

# Create subdirectories 
for subdir in subdirs:
    subdir_path = os.path.join(project_dir, subdir)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)

# Create the work notebook
notebook_name = 'spotify_analysis.ipynb'
notebook_path = os.path.join(project_dir, 'notebooks', notebook_name)

if not os.path.exists(notebook_path):
    with open(notebook_path, 'w') as nb:
        nb.write(f'# Spotify Popularity Analysis\n\n')


