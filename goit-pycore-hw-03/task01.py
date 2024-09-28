from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        difference = datetime.today() - date
        return difference.days
    except ValueError:
        return "Invalid date format. Please, use 'YYYY-MM-DD' format."
