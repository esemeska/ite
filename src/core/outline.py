from descriptors import IntegerValue


class Outline:
    outline_width = IntegerValue(1, 50)
    def __init__(self, is_outline: bool, outline_width, outline_color):
        self.is_outline = is_outline
        self.outline_width = outline_width
        self.outline_color = outline_color

    def is_it_outline(self):
        return self.is_outline

    def to_json(self) -> dict:
        return {
            "is_outline": self.is_outline,
            "outline_width": self.outline_width,
            "outline_color": self.outline_color,
        }
    
    @classmethod
    def from_json(cls, data):
        return Outline(data['is_outline'], data['outline_width'], data['outline_color'])

    def __repr__(self) -> str:
        return f"{self.is_outline}-{self.outline_width}-{self.outline_color}"    