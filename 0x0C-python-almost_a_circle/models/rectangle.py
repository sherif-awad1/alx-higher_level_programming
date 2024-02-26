#!/usr/bin/python3
"""def rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represent rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initi new rectangle
        args:
            width : width of new rectangle
            height: height of the new rectangle
            x : x of rectangle
            y : y of rectangle
            id : id of rectangle
        ris:
            typeerror: If width or height is not int
            valueerror: If width or height = 0
            typeerror: If x or y is not int
            ValueError: Ifx or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set  width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set x  of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """Print rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """update rectangle
        args:
            *args : attribute vlu
                - first: argument id att
                - second: argument width att
                - therd argument height att
                - forth argument x att
                - fivth argument y att
            **kwargs : new key and value
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return dict of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return print() thr rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
