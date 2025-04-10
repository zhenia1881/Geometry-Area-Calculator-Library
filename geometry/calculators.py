from .shapes import Shape

def calculate_area(shape: Shape) -> float:
    return shape.area()

def is_right_angled(shape: Shape) -> bool:
    return shape.is_right_angled()