#test for correct symbol
def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

#test for correct chart type
def validate_chart_type(chart_type):
    return chart_type in {"1", "2"}

#test for time series 
def validate_time_series(time_series):
    return time_series in {"1", "2", "3", "4"}

#test for correct start/end date 
def validate_date(date):
    parts = date.split("-")
    if len(parts) != 3:
        return False
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    return 1000 <= int(year) <= 9999 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31