import os

project_dir = os.getcwd()
subdirs = ['data', 'notebook']

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

# Create a requirements.txt file and add dependencies
with open(os.path.join(project_dir, 'requirements.txt'), 'w') as requirements_file:
    requirements_file.write("pandas\n")
    requirements_file.write("numpy\n")
    requirements_file.write("matplotlib\n")
    requirements_file.write("seaborn\n")
    requirements_file.write("plotly\n")
    requirements_file.write("scikit-learn\n")
    requirements_file.write("ipywidgets\n")
    requirements_file.write("statsmodels\n")  


