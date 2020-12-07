class Room:
    def __init__(self, code, size: int, price: int, longitude: float, latitude: float):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, dictionary):
        return Room(
            code=dictionary["code"],
            size=dictionary["size"],
            price=dictionary["price"],
            longitude=dictionary["longitude"],
            latitude=dictionary["latitude"],
        )

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
