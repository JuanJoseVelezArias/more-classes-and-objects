class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError ("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError ("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        self.__height = value
        
    def area(self):
        return 0 if self.__width == 0 or self.__height == 0 else self.__width * self.__height
  
    def perimeter(self):
        return 0 if self.__width == 0 or self.__height == 0 else (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        figure = ""
        i = 0
        for i in range(self.__height):
            figure += "#" * int(self.__width) + "\n"
        return figure
    def __repr__(self):
        return f"Rectangle('{self.__width}', {self.__height})"