from lib.decorator import print_before


class Rectangle:

    def __init__(self):
        print("==== Rectangle patterns examples ====")

    """
    * * * * *
    * * * * *
    * * * * *
    """

    @print_before
    def solid_rectangle(self, n, columns):
        for _ in range(n):
            for _ in range(columns):
                print("*", end=" ")
            print()

    """
    * * * * *
    *       *
    *       *
    * * * * *
    """

    @print_before
    def hollow_rectangle(self, n, columns):
        for row in range(n):
            for column in range(columns):
                if row == 0 or row == n - 1 or column == columns - 1 or column == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
