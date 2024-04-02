from core.descriptors import IntegerValue


class Dot:
    dot_size = IntegerValue(1, 30)

    def __init__(self, is_dot: bool, size, color):
        self.is_dot = is_dot
        self.dot_size = size
        self.dot_color = color

    def is_it_dot(self) -> bool:
        return self.is_dot
    
    def to_json(self) -> dict:
        return {
            "is_dot": self.is_dot,
            "dot_size": self.dot_size,
            "dot_color": self.dot_color,
        }
    
    @classmethod
    def from_json(cls, data):
        return Dot(data['is_dot'], data['dot_size'], data['dot_color'])

    def __repr__(self) -> str:
        return f"{self.is_dot}-{self.dot_size}-{self.dot_color}"    
