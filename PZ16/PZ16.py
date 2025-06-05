#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте методы для определения дня недели, проверки на високосный год и определения количества дней в месяце.

class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getWeekday(self):
        totalDays = self.day
        monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.isLeapYear():
            monthsDays[1] = 29
        
        for y in range(1, self.year):
            totalDays += 366 if self.isLeapYear(y) else 365
        
        for m in range(self.month - 1):
            totalDays += monthsDays[m]
        
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[(totalDays - 1) % 7]
    
    def isLeapYear(self, year=None):
        if year is None:
            year = self.year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def daysInMonth(self):
        monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            monthsDays[1] = 29
        return monthsDays[self.month - 1]

cal = Calendar(2025, 3, 25)
print("День недели:", cal.getWeekday())
print("Високосный год:", cal.isLeapYear())
print("Количество дней в месяце:", cal.daysInMonth())