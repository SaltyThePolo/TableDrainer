import sys
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def main():

    if (len(sys.argv) == 1 or sys.argv[1] == '-h'):
        print("usage: python3 tableDrainer {url} {filename}")
    else:

        #url dal quale ricavare le tabelle
        page = requests.get(sys.argv[1])

        #parsing del sito
        soup = bs(page.text, "lxml")

        tables = soup.findAll("table")

        counter = 1

        for table1 in tables:
            headers = []
            for i in table1.find_all("th"):
                title = i.text
                headers.append(title)

            mydata = pd.DataFrame(columns = headers)

            for j in table1.findAll("tr")[1:]:
                row_data = j.findAll("td")
                row = [i.text for i in row_data]
                length = len(mydata)
                mydata.loc[length] = row

            file_name = sys.argv[2] + "_" + str(counter) + ".csv"
            mydata.to_csv(file_name, index=False)
            counter = counter + 1

        print('created', str(counter), "files")

# chiamata della funzione "main" quando viene eseguito il programma
if __name__ == "__main__":
    main()