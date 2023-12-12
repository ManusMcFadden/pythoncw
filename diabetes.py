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
                self.data = [row for row in reader]
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
            html.write("<th colspan=\"2\">Positive</th>\n")
            html.write("<th colspan=\"2\">Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("<th>Yes</th>\n")
            html.write("<th>No</th>\n")
            html.write("</tr>\n")
            columncount = 2
            while columncount < self.get_dimension()[1] - 2:
                html.write("<tr>\n")
                html.write("<th>"+self.header[columncount]+"</th>\n")
                rowcount = 0
                pyes = 0
                pno = 0
                nyes = 0
                nno = 0
                while rowcount < self.get_dimension()[0] - 1:
                    if self.data[rowcount][self.get_dimension()[1] - 1] == "Positive":
                        if self.data[rowcount][columncount] == "Yes":
                            pyes += 1
                        else:
                            pno +=1
                    else:
                        if self.data[rowcount][columncount] == "Yes":
                            nyes += 1
                        else:
                            nno +=1
                    rowcount += 1
                html.write("<th>"+str(pyes)+"</th>\n")
                html.write("<th>"+str(pno)+"</th>\n")
                html.write("<th>"+str(nyes)+"</th>\n")
                html.write("<th>"+str(nno)+"</th>\n")
                html.write("</tr>\n")
                columncount += 1
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
