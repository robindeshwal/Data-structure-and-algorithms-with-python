from .pyramid import Pyramid
from .diamond import Diamond
from .rectangle import Rectangle
from .miscleneous import Miscleneous

rows = int(input("Enter your value for rows: "))
columns = int(
    input("Enter your value for columns (optional, default 6): ") or "6")

# Rectangle patterns:
rectangle_obj = Rectangle()
rectangle_obj.solid_rectangle(rows, columns)
rectangle_obj.hollow_rectangle(rows, columns)

# Pyramid patterns:
pyramid_obj = Pyramid()
# pyramid_obj.full_pyramid(rows)
# pyramid_obj.half_pyramid_stars(rows)
# pyramid_obj.half_pyramid_numbers(rows)
# pyramid_obj.inverted_full_pyramid(rows)
# pyramid_obj.inverted_half_pyramid(rows)
# pyramid_obj.hollow_full_pyramid(rows)
# pyramid_obj.alphabet_palindrome_pyramid(rows)
# pyramid_obj.numeric_full_pyramid(rows)
# pyramid_obj.numeric_hollow_pyramid(rows)

# # Diamond patterns:
# diamond_obj = Diamond()
# diamond_obj.full_diamond(rows)
# diamond_obj.hollow_diamond(rows)

# # Miscleneous patterns:
# miscleneous_obj = Miscleneous()
# miscleneous_obj.fancy_pattern(rows)
