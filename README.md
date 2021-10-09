# Correlates of War

Jenna Jordan

## About

The Correlates of War Project is a collection of datasets that tracks wars and conflicts across the world since 1816. These datasets are commonly used by political scientists interested in peace & conflict studies. To learn more about the Correlates of War (CoW), please visit their website: https://correlatesofwar.org/

This project does a few different things with the Correlates of War datasets:

- clean and re-organize the datasets into a tidy format
- create a relational database in which to store all the CoW data
- visualize the CoW data with interactive plots on a Streamlit web app

This project builds on previous work I have done with the Correlates of War data in the following repos:

- [international-relations-database](https://github.com/jenna-jordan/international-relations-database)
- [international-relations-database-extended](https://github.com/jenna-jordan/international-relations-database-extended)
- [IS590DV-FinalProject](https://github.com/jenna-jordan/IS590DV-FinalProject)

## Environment

Steps to recreate environment used for this repo:

1. Create new environment with conda, e.g. named "cow"
    - `conda create --name cow python=3.9` 
    - `conda activate cow`
2. Install streamlit (and a bunch of other packages that are dependencies)
    - `conda install -c conda-forge streamlit`
3. Install plotly (according to the [documentation](https://plotly.com/python/getting-started/#installation))
    - `conda install -c plotly plotly=5.3.1`
    - `conda install -c plotly plotly-geo=1.0.0`
4. Install sqlmodel
    - `conda install -c conda-forge sqlmodel`
5. Install black (for code formatting)
    - `conda install -c conda-forge black`
6. Install jupyterlab
    - `conda install -c conda-forge jupyterlab`

And add the kernel so we can work in Jupyter Lab:

`python -m ipykernel install --user --name cow`

## Repo Structure

### Directories

- All datasets are kept in the `Data` directory. Raw datasets - downloaded directly from the source and not altered in any way - are kept in the `Data/Raw` subdirectory.
- All data documentation is kept in the `Documentation` directory. Raw documentation - PDFs downloaded directly from the source and not altered in any way - are kept in the `Documentation/Raw` subdirectory.
- Code for wrangling data (manipulating it into the format needed by the database) is kept in the `Wrangle` directory
- Code for creating and manipulating the database is kept in the `Database` directory

### Files in root directory

- All dataset and documentation citations are kept in `CITATIONS.md`
- The license, found at `LICENSE`, is a BSD 3-Clause License with an addendum for the Correlates of War Project's Terms & Conditions

## Datasets

All datasets were downloaded from the [Correlates of War website](https://correlatesofwar.org/). The raw datasets were saved to `Data/Raw`. Accompanying documentation were saved to `Documentation/Raw`. These files have not been altered in any way. The requested citations for these datasets have been included in `CITATIONS.md`.

- COW Country Codes
    - Downloaded from: `https://correlatesofwar.org/data-sets/cow-country-codes`
    - Downloaded on: `2021-07-17`
    - Data Filename(s): `COW country codes.csv`
    - Documentation Filename(s): n/a

- State System Membership (v2016)
    - Downloaded from: `https://correlatesofwar.org/data-sets/state-system-membership`
    - Downloaded on: `2021-07-17`
    - Data Filename(s): `states2016.csv`, `majors2016.csv`, `system2016.csv`
    - Documentation Filename(s): `State System Membership Codebook V2016.pdf`, `State FAQ.pdf`

- COW War Data, 1816 - 2007 (v4.0)
    - Downloaded from: `https://correlatesofwar.org/data-sets/COW-war`
    - Downloaded on: `2021-07-17`
    - Documentation Filename(s): `CowWarList.pdf`, `COW Website - Typology of war.pdf`

    - **Non-State Wars**
        - Data Filename(s): `Non-StateWarData_v4.0.csv`
        - Documentation Filename(s): `Non-StateWars_Codebook.pdf`, `Non-StateWarsList.pdf`

    - **Intra-State Wars**
        - Data Filename(s): `INTRA-STATE WARS v5.1 CSV.csv`, `INTRA-STATE_State_participants v5.1 CSV.csv`
        - Documentation Filename(s): `Codebook for Intra-state v5.1 2.9.20.pdf`, `Description of Intra-state v5.1.pdf.pdf`

    - **Inter-State Wars**
        - Data Filename(s): `Inter-StateWarData_v4.0.csv`
        - Documentation Filename(s): `Inter-StateWarsList.pdf`, `Inter-StateWars_Codebook.pdf`

    - **Extra-State Wars**
        - Data Filename(s): `Extra-StateWarData_v4.0.csv`
        - Documentation Filename(s): `Extra-StateWars_Codebook.pdf`

- National Material Capabilities (v5.0)
    - Downloaded from: `https://correlatesofwar.org/data-sets/national-material-capabilities`
    - Downloaded on: `2021-07-17`
    - Data Filename(s): `NMC_5_0.csv`, `NMC_5_0-wsupplementary.csv`
    - Documentation Filename(s): `NMC_Documentation_v5_0.pdf`