import csv

filename = "C:/Users/umesh/Downloads/bigBasketProductList/BigBasket Products.csv"

fields = []
rows = []

with open(filename,'r',encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    # creating a csv reader object
    fields = next(csv_reader)
    # extracting each data row one by one
    for row in csv_reader:
        rows.append(row)

    # get total number of rows
    print(f'total no of rows {csv_reader.line_num}')
    for row in rows[:5]:
        for col in row:
            print(f"{col}", end="|")
        print()
