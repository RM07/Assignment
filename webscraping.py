import bs4 as bs
import urllib.request
import csv

source = urllib.request.urlopen('http://books.toscrape.com/').read()
soup = bs.BeautifulSoup(source,'lxml')

book_info = soup.find_all('li',class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

# array1 = []
# array2 = []
# array3 = []

# for book in book_info:

#     array1.append(book.find('h3').find('a').get('title'))


# for book in book_info:
#     array2.append(book.find('div',class_='product_price').find('p',class_='price_color').text)


# for book in book_info:
#     array3.append(book.find('p',class_='star-rating').get('class')[1])


# for i in range(len(book_info)):
#     print(array1[i])
#     print(array2[i])
#     print(array3[i])

#     print("-----------------------------------------------------------------")
fields = ['title','price','no_of_start']
DataArray = []
for book in book_info:
    arr = []
    arr.append(book.find('h3').find('a').get('title'))
    arr.append(book.find('div',class_='product_price').find('p',class_='price_color').text)
    arr.append(book.find('p',class_='star-rating').get('class')[1])

    DataArray.append(arr)


filename = 'rohan.csv'
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(DataArray)


