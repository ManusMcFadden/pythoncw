"""
Please write your name
@author: Manus McFadden

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        try:
            with open(filepath) as file:
                # filepath passed is the filename to be opened
                reader = csv.reader(file)  # read the csv file
                self.header = next(reader)  # make top row the list of headers
                # make the rest of the rows into the data
                self.data = [row for row in reader]
        except FileNotFoundError:  # output error if file cannot be opened
            print("File not found.")

    def get_dimension(self) -> list:
        rows = len(self.data)  # rows is the length of the data list
        columns = len(self.header)  # columns is the length of the header list
        return [rows, columns]

    def web_summary(self, filepath: str) -> None:
        # open the file that the html will
        # be written to with the name as the filepath passed to it
        with open(filepath, "w") as html:
            html.write("<html>\n")
            html.write("<table>\n")
            html.write("<tr>\n")
            # create the table headings
            html.write("<th rowspan=\"3\">Attributes</th>\n")
            html.write("<th>Class</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th colspan=\"2\">Positive</th>\n")
            html.write("<th colspan=\"2\">Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("</tr>\n")
            columncount = 2  # skipping age and gender
            while columncount < self.get_dimension()[1] - 2:  # skipping class
                html.write("<tr>\n")  # make new rows for every new header
                # write the header name
                html.write("<th>"+self.header[columncount]+"</th>\n")
                rowcount = 0
                # initialise number of yes and no answers
                pyes = 0
                pno = 0
                nyes = 0
                nno = 0
                # iterate through each row
                while rowcount < self.get_dimension()[0] - 1:
                    # check last value for p/n
                    if self.data[rowcount][self.get_dimension()[1] - 1] == "Positive":
                        if self.data[rowcount][columncount] == "Yes":
                            # add total number of y/n
                            pyes += 1
                        else:
                            pno += 1
                    else:
                        if self.data[rowcount][columncount] == "Yes":
                            nyes += 1
                        else:
                            nno += 1
                    rowcount += 1
                # write total number of y/n to table
                html.write("<th>"+str(pyes)+"</th>\n")
                html.write("<th>"+str(pno)+"</th>\n")
                html.write("<th>"+str(nyes)+"</th>\n")
                html.write("<th>"+str(nno)+"</th>\n")
                html.write("</tr>\n")
                columncount += 1
            html.write("</table>\n")
            html.write("</html>\n")

    '''Input a dictionary of header and data to the count instances
      function and it will return the number of instances with
        all of this data as an integer'''

    def count_instances(self, criteria: dict) -> int:
        count = 0
        for row in self.data:  # iterate through each row
            found = True
            for key, value in criteria.items():
                # check if the values in each column
                #  are the same as the criteria data
                iCol = self.header.index(key)
                if row[iCol] != str(value):
                    found = False
                    break
            if found:  # if all the criteria are met add one to the count
                count += 1
        return count


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    print(d1.count_instances({"Age": 30, "Gender": "Female", "Obesity": "No"}))
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    print(d2.count_instances({"Gender": "Male", "Itching": "Yes"}))
