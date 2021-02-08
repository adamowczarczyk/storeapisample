Sample dummy store api backend.

Written in FastAPI, sqlite, pandas.

Tests using pytest and tavern.

Versioning using custom headers.

To create environment, run conda env create -f environment.yml

To run the api, run uvicorn main:app --reload

Should be available under http://127.0.0.1:8000/docs