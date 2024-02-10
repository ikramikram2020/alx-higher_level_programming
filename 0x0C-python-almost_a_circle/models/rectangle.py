from models.base import Base
class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If any argument is not an int.
            ValueError: If any argument is <= 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        self.validate_int_value(value, "width")
        self.validate_positive_value(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        self.validate_int_value(value, "height")
        self.validate_positive_value(value, "height")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle."""
        self.validate_int_value(value, "x")
        self.validate_non_negative_value(value, "x")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle."""
        self.validate_int_value(value, "y")
        self.validate_non_negative_value(value, "y")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def validate_int_value(self, value, attr_name):
        """Validate if value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

    def validate_positive_value(self, value, attr_name):
        """Validate if value is positive."""
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def validate_non_negative_value(self, value, attr_name):
        """Validate if value is non-negative."""
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")
