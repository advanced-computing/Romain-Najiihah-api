import pandas as pd

film_permits = pd.read_csv("Film_Permits_20260213.csv")


def EventAgency():
    film_permits_copy = film_permits.copy()
    film_permits_copy["EventAgency"] = film_permits_copy["EventAgency"].replace(
        {"Mayor's Office of Media & Entertainment": "Mayor's office"}
    )
    return film_permits_copy


def borough():
    film_permits_copy = film_permits.copy()
    film_permits_copy["Borough"] = film_permits_copy["Borough"].str.upper()
    return film_permits_copy


def entered_on():
    film_permits_copy = film_permits.copy()
    film_permits_copy["EnteredOn"] = film_permits_copy["EnteredOn"].fillna("Unknown")
    return film_permits_copy
