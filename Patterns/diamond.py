from lib.decorator import print_before


class Diamond:

    def __init__(self):
        print("==== Diamond patterns examples ====")

    """
        *
       * *
      * * *
     * * * *
    * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
    """

    @print_before
    def full_diamond(self, n):
        for row in range(n):
            for col in range(n):
                temp = ""
                if col < (n - row) - 1:
                    temp += " "
                else:
                    temp += "* "
                print(temp, end="")
            print()
        for row in range(n):
            for col in range(n):
                temp = ""
                if col < row:
                    temp += " "
                else:
                    temp += "* "
                print(temp, end="")
            print()

    """
        *
       * *
      *   *
     *     *
    *       *
    *       *
     *     *
      *   *
       * *
        *
    """

    @print_before
    def hollow_diamond(self, n):
        for row in range(n):
            temp = ""
            for _ in range((n - row) - 1):
                temp += " "
            for col in range((2 * row) + 1):
                if col == 0 or col == 2 * row:
                    temp += "*"
                else:
                    temp += " "
            print(temp, end="")
            print()
        for row in range(n):
            temp = ""
            for col in range(row):
                temp += " "
            for col in range(2 * (n - row - 1) + 1):
                if col == 0 or col == 2 * (n - row - 1):
                    temp += "*"
                else:
                    temp += " "
            print(temp, end="")
            print()

    """
    * * * * *  * * * * *
    * * * *      * * * *
    * * *          * * *
    * *              * *
    *                  *
    *                  *
    * *              * *
    * * *          * * *
    * * * *      * * * *
    * * * * *  * * * * *
    """

    @print_before
    def flipped_solid_diamond(self, n):
        pass
