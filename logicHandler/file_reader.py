import csv
import pandas as pd
import xlrd

class Emailaddress:
    def __init__(self):
        self.address = list()

    def unpack_address(self,filename):
        if filename.endswith('.xlsx'):
            file = xlrd.open_workbook(filename)
            sheet = file.sheet_by_name('Sheet1')
            self.address.clear()
            for value in sheet.col_values(0):
                if isinstance(value,str):
                    self.address.append(value)
            self.address.pop(0)

        elif filename.endswith('.csv'):
            with open(f"{filename}") as file:
                csv_reader = csv.DictReader(file)
                self.address.clear()
                for e in csv_reader:
                    self.address.append(e['emails'])



unpack = Emailaddress()