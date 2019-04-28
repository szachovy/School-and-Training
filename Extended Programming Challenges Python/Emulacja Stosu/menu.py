
class Menu(object):
    @classmethod
    def starter(cls):
        return "Welcome in stack emulation program, results will be saved in stosdb" \
               "\nHere are the oprions supported by the program\n" \
               "1. Push item\n" \
               "2. Pop item\n" \
               "3. Check that selected item is in the stack\n" \
               "4. Get stack size\n" \
               "5. Print all elements whose are currently in stack\n" \
               "6. Exit program\n"

    @classmethod
    def choose(cls) -> int:
        choice = input("What do you want with stack ? : ")
        try:
            choice = int(choice)
            if choice in range(1, 7):
                return choice
            else:
                print('Wrong range of value, retry')
        except ValueError:
            print('int is expected, retry')
        return Menu.choose()


