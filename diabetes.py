"""
Please write your name
@author:

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        try:
            with open(filepath) as file:
                reader = csv.reader(file)
                self.header = next(reader)
                for row in reader:
                    self.data = row
        except FileNotFoundError:
            print("File not found.")

    def get_dimension(self) -> list:
        rows = len(self.data)
        columns = len(self.header)
        return [rows, columns]

    def web_summary(self, filepath: str) -> None:
        with open(filepath,"w") as html:
            html.write("<html>\n")
            html.write("<table>\n")
            html.write("<tr>\n")
            html.write("<th rowspan=\"3\">Attributes</th>\n")
            html.write("<th>Class</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th>Positive</th>\n")
            html.write("<th>Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("</tr>\n")
            count = 2

            while count1 < columns - 1:
                html.write("<tr>\n")
                html.write("<th>"+self.header[count1]+"</th>\n")
                count2 = 1
                yes = 0
                no = 0
                while count2 < rows:
                    if self.data[count2] = yes count 
                html.write("<th>"+
                html.write("</tr>\n")
                count += 1
            html.write("</table>\n")
            html.write("</html>\n")


    def count_instances(self, criteria) -> int:
        # delete pass and this line to write your code
        # you can change the parameter criteria or the number of parameters
        # as you want, provided they are explained in doctring for this
        # method
        pass


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
