#Three sides form a triangle when the sum of any two sides is greater than the third;
  #  Equilateral Triangle: three equal sides;
  #  Isosceles Triangle: any two equal sides;
  #  Scalene Triangle: three different sides.


def type_of_triangle(side1, side2, side3):
    is_triangle = (
            side1 + side2 > side3 and
            side2 + side3 > side1 and
            side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"