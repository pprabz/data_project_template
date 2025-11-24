📘 Data Project Template

A reusable, professional template for data analysis, EDA, modeling, and visualization workflows.

This repository provides a standard folder structure, starter notebooks, and requirements for any data project.
It ensures consistency, clean organization, and reproducibility — aligned with how companies structure data science projects.

🚀 Features of This Template
✔ Predefined folder structure
project/
├── data_raw/          → Original untouched datasets  
├── data_processed/    → Cleaned / transformed datasets  
├── notebooks/         → Ready-to-use Jupyter templates  
├── scripts/           → Reusable Python utilities & SQL cleaning script  
├── outputs/           → Charts, reports, model files  
└── config/            → requirements.txt and environment-related files

✔ Ready-to-run notebooks

01_eda_template.ipynb – Exploratory Data Analysis

02_modeling_template.ipynb – ML starter pipeline

03_visualization_template.ipynb – Plotting & dashboards

✔ Optimized requirements.txt

Includes: pandas, numpy, sklearn, matplotlib, seaborn, duckdb, pyarrow, profiling tools, etc.

✔ Git-friendly

.gitignore file included

Raw data folders excluded from version control

🏗️ How This Template Was Created

Creating template was built to provide a clean, repeatable structure for data projects.
Steps used to create it:
1️⃣ Create a reusable template folder
In Termial

```bash
mkdir -p ~/templates/data_project_template
cd ~/templates/data_project_template

mkdir -p data_raw data_processed notebooks scripts outputs config

```

Created folder structure:
```text
data_raw/
data_processed/
notebooks/
scripts/
outputs/
config/
```
** This folder will NEVER be used directly for work — only copied.

2️⃣ Add a reusable requirements.txt
```bash
nano config/requirements.txt
```
```text
pandas
numpy
matplotlib
seaborn
scikit-learn
pyarrow
openpyxl
jupyterlab
```
Save (Ctrl+O, Enter) and exit (Ctrl+X).

3️⃣ Add your EDA notebook template

Activate your env & open Jupyter in the template folder:
```bash
conda activate aihc_env
cd ~/templates/data_project_template
jupyter lab
```


In JupyterLab:

Go to notebooks/

Create a new notebook

create and Save it as:
01_eda_template.ipynb

That’s now your master EDA template.

Added:

Templates for EDA, modeling, visualization

requirements.txt

utils.py + SQL cleaning script

README.md

.gitignore to avoid committing datasets

Uploaded the folder to GitHub as a Template Repository
(GitHub → Settings → General → Enable “Template repository”)

This allows anyone to click “Use this template” to start a new project instantly.

📦 How to Use This Template (Step by Step)
1️⃣ Create a new project from the template

Go to this repository on GitHub → Click:

Use this template → Create a new repository


Example new repository name:

customer-analysis-2025


This creates a clean copy of the template as a new project.

2️⃣ Clone your new project to your computer
cd ~/projects
git clone https://github.com/YOUR_USERNAME/customer-analysis-2025.git
cd customer-analysis-2025

3️⃣ Activate your Conda environment
`conda activate aihc_env

4️⃣ Install all required libraries
`pip install -r config/requirements.txt


This installs:

pandas, numpy, matplotlib

seaborn, sklearn

duckdb, SQLAlchemy

ydata-profiling, missingno

jupyterlab
…and more.

5️⃣ Add Data

Place your raw dataset files in:

data_raw/


Example:

data_raw/customers.csv

6️⃣ Start working using Jupyter
jupyter lab


Start with:

notebooks/01_eda_template.ipynb

Update DATA_PATH inside the notebook

Run the full EDA pipeline

Then continue with:

02_modeling_template.ipynb

03_visualization_template.ipynb

🔄 Sync Changes Back to GitHub (Version Control Workflow)

Inside your project folder:

1. Check what changed
git status

2. Add changes
git add .

3. Commit those changes
git commit -m "Describe what you changed: e.g., added EDA and cleaned data"

4. Push changes to GitHub
git push


Now GitHub gets updated with:

your notebooks

your scripts

your visualizations

your progress

(Datasets will not be uploaded because they live in data_raw/ and are ignored — which is good.)

🧭 Typical Company-Style Workflow

Create new project from template

Clone locally

Create a clean branch (optional but recommended)

Activate environment

Install dependencies

Add data to data_raw/

Perform EDA

Clean & transform data → save in data_processed/

Feature engineering

Use modeling or visualization template

Commit & push progress often

Share results or merge branches

Repeat process for next project

🧱 Best Practices
✔ Never edit the original template; clone from GitHub each time
✔ Never commit datasets (template already ignores them)
✔ Always write meaningful commit messages
✔ Keep notebooks clean and organized
✔ Keep reusable functions in scripts/utils.py
✔ Export cleaned CSVs to data_processed/
✔ Use one Conda environment (aihc_env) for all projects
🤝 Contributing / Improving the Template

If you improve:

the EDA process

modeling code

visualization workflow

utils scripts

requirements.txt

…then update this template repo, so all future projects benefit.

You can either:

Push changes directly (if you own the repo)

Or fork → improve → open a pull request

🎉 Summary

This template helps you:

Start every project quickly

Maintain consistent structure

Avoid messy folders

Reuse a tested workflow

Stay aligned with data engineering best practices

Easily collaborate on GitHub

Keep raw and processed data separate

Make your work reproducible