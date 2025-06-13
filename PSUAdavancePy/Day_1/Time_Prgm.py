class Time:
    def __init__(self,year,month):
        self.year = year + month // 12
        self.month = month % 12
    def __add__(self,other):
        total_y = self.year + other.year
        total_m = self.month + other.month
        if total_m >= 12:
            total_y = total_y + total_y // 12
            total_m = total_m % 12
        return Time(total_y , total_m)
    def __repr__(self):
        return f"{self.year} years and {self.month} months"
time1 = Time(21,56)
time2 = Time(14,25)
time = time1 + time2
print(time)