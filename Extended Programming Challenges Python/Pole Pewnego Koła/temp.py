"""Pierwsza opcja"""
def create_file(filename: str, start_value):
    # Tworzymy pusty plik
    # Zapisujemy wartość startową
    f = open(filename, "w")
    f.write(str(start_value))
    f.close()
    return start_value


def get_var_value(filename: str = "varstore.dat", start_value=1):
    try:
        with open(filename, "r+") as f:
            # odczytujemy plik
            file_date = f.read()
            if file_date == "":  # kiedy plik jest PUSTY
                return create_file(filename, start_value)

            # Czyścimy plik
            f.seek(0)
            f.truncate(0)

            try:
                # Zapisujemy
                f.write(str(int(file_date) + 1))
            except ValueError:
                # Kiedy w pliku było by coś co nie jest liczbą
                # Inicjujemy go ponownie
                return create_file(filename, start_value)

            f.close()
            return int(file_date) + 1
    except FileNotFoundError:
        # kiedy plik nie istnieje
        return create_file(filename, start_value)


counter = get_var_value()
print("Ilosc wykonan programu -> {}".format(counter))

"""Druga opcja"""

def get_var_value(filename: str = "varstore.dat"):
    counter = 0
    try:
        with open(filename, "r+") as f:
            file_counter = f.read()
            if not file_counter:
                raise FileNotFoundError()
            else:
                counter = int(file_counter) + 1
            f.seek(0)
            f.truncate()
            f.write(str(counter))
    except (ValueError, FileNotFoundError) as e:
        with open(filename, "w") as f:
            counter += 1
            f.write(str(counter))
    return counter


if __name__ == '__main__':
    counter = get_var_value()
    print("Ilosc wykonan programu -> {}".format(counter))