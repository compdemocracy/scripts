# pol.is Scripts

Scripts to streamline the running of the pol.is instance used in Policy Lab. Some of these will become features later on.

## Getting Started

Most scripts require [Anaconda Python environment](https://www.anaconda.com/) to be installed. Once installed, setup a virtual environment using

```
python -m venv .venv --system-site-packages
```

in the root folder. This lets you install additional Python packages without interfering with the main Anaconda installation.

You may need to select the local `.venv` interpreter in your IDE at this point to run the virtual environment Python install.

Once this is done, run

```
pip install -r requirements.txt
```

We also don't want to include output of the notebooks in Git for GDPR reasons. To avoid this run 

```
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'
```

Individual script folders will contain further instructions particular to that script.

## Conventions

* To avoid checking PII or secrets into Git ...
  * Use a `.env` file for secrets
  * Use `data` folder for input files
  * Name output files `<something>.output.csv`
* Sometimes you may want to manually clean up data so that the script can read it. Rename the original input file with `<filename>.original.<extension>` and create a copy called `<filename>.cleanedup.<extension>` for the file containing edits. Both will be ignored by Git.
* If you need a new library installing, add it to the root `requirements.txt`

There are some common environment variables used in the scripts
| Name | Description |
| --- | --- |
| `CONVERSATION_ID` | The characters after the slash on the conversation page e.g. `9rak4kaysm` |
| `DRY_RUN` | Set to `true` for the script to execute but not make any changes so you can check the output |
| `POLIS_USERNAME` | The username for an account that owns the particular debate |
| `POLIS_PASSWORD` | The password for an account that owns the particular debate |
| `POLIS_API_BASE_URL` | The URL for the pol.is API without trailing slash e.g. `https://pol.is/api/v3` |
