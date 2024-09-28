from collections import UserDict
from record import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of Record")
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.date[name]
        else:
            raise ValueError("Record not found")
        
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        current_date = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=current_date.year)

                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

                if 0 <= (birthday_this_year - current_date).days <= 7:
                    if birthday_this_year.weekday() == 5:
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:
                        birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays