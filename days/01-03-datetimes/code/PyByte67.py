from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date(start_date):
    """Return a string of yyyy-mm-dd"""
    end_date = start_date + timedelta(100)
    return str(end_date)


get_hundred_days_end_date(start_100days)


def get_days_between_pb_start_first_joint_pycon(start_date, end_date):
    """Return the int number of days"""
    diff = end_date - start_date
    return diff.days

get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date)


