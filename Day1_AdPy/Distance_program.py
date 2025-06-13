class Distance:
    def __init__(self, km=0, m=0):
        # Ensure that meters are always less than 1000
        self.km = km + m // 1000
        self.m = m % 1000

    def __add__(self, other):
        # Add the kilometers and meters separately
        total_km = self.km + other.km
        total_m = self.m + other.m

        # If grams exceed 1000, convert to kilograms
        if total_m >= 1000:
            total_km += total_m // 1000
            total_m = total_m % 1000

        return Distance(total_km, total_m)

    def __repr__(self):
        return f"{self.km} km and {self.m} m"

# Example usage
dist1 = Distance(2, 500)  # 2 km 500 m
dist2 = Distance(1, 750)  # 1 km 750 m

dist3 = dist1 + dist2
print(dist3)