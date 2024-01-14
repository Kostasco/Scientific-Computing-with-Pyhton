class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def set_width(self, width):
      self.width = width

  def set_height(self, height):
      self.height = height

  def get_area(self):
      return self.width * self.height

  def get_perimeter(self):
      return 2 * self.width + 2 * self.height

  def get_diagonal(self):
      return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
        return "Too big for picture."
    else:
        hori_line = '*' * self.width + '\n'
        inner_lines = ('*' * self.width + '\n') * (self.height - 2)
        return hori_line + inner_lines + hori_line


  def get_amount_inside(self, shape):
      return int(self.width / shape.width) * int(self.height / shape.height)

  def __str__(self):
      return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
  def __init__(self, side_length):
      super().__init__(side_length, side_length)

  def set_side(self, side_length):
      self.set_width(side_length)
      self.set_height(side_length)

  def set_width(self, width):
      self.width = width

  def set_height(self, height):
      self.height = height

  def __str__(self):
      return f"Square(side={self.width})"
