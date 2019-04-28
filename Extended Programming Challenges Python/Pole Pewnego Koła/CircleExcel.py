import xlsxwriter
import math
from xlrd import open_workbook
from xlutils.copy import copy

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
    setResults = {}

    r = float(input('insert radiation of sphere'))
    setResults[0] = r
    d = float(input('mark distance between spheres centre'))
    setResults[1] = d

    new_r = math.sqrt((r * r) - (0.25 * d * d))
    P = math.pi*new_r**2

    setResults[2] = P
    print(P)

    try:
        book_ro = open_workbook('results.xlsx')
        book = copy(book_ro)
        sheet1 = book.get_sheet(0)

        for i in setResults.keys():
            sheet1.write(counter, 0, 'attept->' + str(counter))
            sheet1.write(counter, i + 1, setResults[i])

        book.save('results.xlsx')

    except FileNotFoundError:
        workbook = xlsxwriter.Workbook('results.xlsx')

        worksheet = workbook.add_worksheet('calculations')
        worksheet.write(0, 1, 'RADIATION')
        worksheet.write(0, 2, 'SPHERES DISTANCE')
        worksheet.write(0, 3, 'RESULT')

        for i in setResults.keys():
            worksheet.write(counter, 0, 'attept->' + str(counter))
            worksheet.write(counter, i + 1, setResults[i])

        workbook.close()

