import csv
filename = "C:/Users/umesh/Downloads/bigBasketProductList/BigBasket Products.csv"
with open(filename, 'r', encoding="utf-8") as csvfile:
    reader_data = csv.reader(csvfile, delimiter='\t')
    print(type(reader_data))
    for row in reader_data:
        print(row)
