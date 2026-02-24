from film_helper import EventAgency
from film_helper import borough
from film_helper import entered_on


def test_EventAgency():
    df = EventAgency()
    assert "EventAgency" in df.columns
    assert df["EventAgency"].str.contains("Mayor's office").any()


def test_fix_borough():
    df = borough()
    assert "Borough" in df.columns
    assert df["Borough"].str.upper().equals(df["Borough"])


def test_fix_entered_on():
    df = entered_on()
    assert "EnteredOn" in df.columns
    assert df["EnteredOn"].isna().sum() == 0
