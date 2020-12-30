import datetime


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = datetime.date.today()#.strftime("%d.%m.%Y")
        else:
            self.date = datetime.datetime.strptime(date, "%d.%m.%Y").date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        now = datetime.date.today()#.strftime("%d.%m.%Y")
        amount_sum = 0
        for item in self.records:
            if item.date == now:
                amount_sum += item.amount
        return amount_sum

    def get_week_stats(self):
        week = datetime.date.today() - datetime.timedelta(days=7)
        amount_sum = 0
        for record in self.records:
            if record.date >= week:
                amount_sum += record.amount
        return amount_sum


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        if self.get_today_stats() >= self.limit:
            answer = "Хватит есть!"
        elif self.get_today_stats() < self.limit:
            answer = "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {} кКал".format(self.limit - self.get_today_stats())
        return answer


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    USD_RATE = 74.
    EURO_RATE = 92.

    def get_today_cash_remained(self, currency):
        difference = self.limit - self.get_today_stats()
        change = {"rub": "руб", "usd": "USD", "eur": "Euro"}

        if difference == 0:
            answer = "Денег нет, держись"
        else:
            if currency == "usd":
                difference = difference / self.USD_RATE
            elif currency == "eur":
                difference = difference / self.EURO_RATE
            difference = float(round(difference, 2))
            if difference < 0:
                answer = "Денег нет, держись: твой долг - {} {}".format(-difference, change[currency])
            elif difference > 0:
                answer = "На сегодня осталось {} {}".format(difference, change[currency])
        return answer
