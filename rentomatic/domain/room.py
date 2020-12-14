from typing import Dict


class Room:
    def __init__(self, code, size: int, price: int, longitude: float, latitude: float) -> None:
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, dictionary: Dict):
        return Room(
            code=dictionary["code"],
            size=dictionary["size"],
            price=dictionary["price"],
            longitude=dictionary["longitude"],
            latitude=dictionary["latitude"],
        )

    def to_dict(self) -> Dict:
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    def __eq__(self, other) -> bool:
        return self.to_dict() == other.to_dict()
