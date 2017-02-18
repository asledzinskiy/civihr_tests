from datetime import date, timedelta


def generate_current_date():
    cur_date = date.today()
    return "{day}/{month}/{year}".format(day=cur_date.strftime("%d"),
                                         month=cur_date.strftime("%m"),
                                         year=cur_date.strftime("%Y"))


def generate_date_future_month():
    next_month_date = date.today() + timedelta(30)
    return "{day}/{month}/{year}".format(day=next_month_date.strftime("%d"),
                                         month=next_month_date.strftime("%m"),
                                         year=next_month_date.strftime("%Y"))


def generate_date_future_day():
    next_day_date = date.today() + timedelta(1)
    return "{day}/{month}/{year}".format(day=next_day_date.strftime("%d"),
                                         month=next_day_date.strftime("%m"),
                                         year=next_day_date.strftime("%Y"))


def generate_half_year_date():
    next_half_year_date = date.today() + timedelta(180)
    return "{day}/{month}/{year}".format(day=next_half_year_date.strftime("%d"),
                                         month=next_half_year_date.strftime("%m"),
                                         year=next_half_year_date.strftime("%Y"))
