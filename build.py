from flask import Flask
from flask import request
import pandas as pd
import duckdb

film_permits = Flask(__name__)

DB_FILE = "film_permit.db"


@film_permits.get("/")
def home():
    return "Server is running. No worries. Choose your path wisely. /api/list is perhaps the one you want to go to."


@film_permits.get("/api/list")
def list():

    # Get the query parameters
    format = request.args.get("format", "csv")
    filterby = request.args.get("filterby", None)
    filtervalue = request.args.get("filtervalue", None)
    limit = int(request.args.get("limit", 1000))
    offset = int(request.args.get("offset", 0))

    # Connect to database
    conn = duckdb.connect(DB_FILE)
    data = conn.execute("SELECT * FROM film_permits").df()
    conn.close()

    # filter the data
    data = filter_by_value(data, filterby, filtervalue)
    if isinstance(data, str):
        return data

    # applying the limit and offset
    data = apply_limit_offset(data, limit, offset)

    # convert the data to the requested format
    data = convert_to_format(data, format)

    return data


@film_permits.get("/api/record/<record_id>")
def get_record(record_id):
    # Load the data
    conn = duckdb.connect(DB_FILE)
    record = conn.execute(
        "SELECT * FROM film_permits WHERE EventID = ?", [int(record_id)]
    ).df()
    conn.close()

    if record.empty:
        return "Record not found"

    # Convert the record to the requested format
    return convert_to_format(record, request.args.get("format", "json"))


def filter_by_value(data, filterby, filtervalue):

    if filterby:
        if filtervalue is None:
            return "Invalid filtervalue"
        elif filterby not in data.columns:
            return "Invalid filterby column"
        else:
            data = data[data[filterby] == int(filtervalue)]
    return data


def apply_limit_offset(data, limit, offset):
    return data.iloc[offset : offset + limit]


def convert_to_format(data, format):
    if format == "json":
        return data.to_json(orient="records")
    elif format == "csv":
        return data.to_csv(index=False)
    else:
        return "Invalid format"


if __name__ == "__main__":
    film_permits.run(debug=True)
