# REDCap API Security Check

This project checks to see if the REDCap API returns any of the fields marked in the project as "identifiers" which often contain protected health information (PHI). The intention is that if the call to the API returns any values other than the record status.

## Requirements

* Python3
* PyCap with data-science extras (Pandas)
* python-dotenv

## Installation

To set up the project, install the requirements:

```
pip install -r requirements.txt
```

Or install using a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
The check requires two environment variables:

* `REDCAP_TOKEN` - the REDCap API token for the project to test
* `REDCAP_URL` - the URL for the REDCap API address for the instance

These variables can optionally be loaded from a `.env`. Copy the `env.example` file to `.env` and add the required values.

## Running

Once all the requirements are met, run the following command:

```
python3 main.py
```

If the number of columns per row is equal two the two standard columns of `redcap_repeat_instrument` and `redcap_repeat_instance` then it exits cleanly. If there are more than two columns then it throws an `AssertionError`.