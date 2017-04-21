import requests
from bs4 import BeautifulSoup
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()  # to disable InsecurePlatformWarning
import lxml
from openpyxl import Workbook  # https://openpyxl.readthedocs.io/en/default/

wb = Workbook()

# grab the active worksheet
ws = wb.active

review_list = []
# it might crawl almost all kinds of facebook pages, you have to give the page reviews link here
url = 'http://www.facebook.com/ajkercrazydeal/reviews/'
source_code = requests.get(url)  # getting the source code of the url
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "lxml")  # creating a BeautifulSoup object(name: soup)
for div in soup.findAll('p'):
    review = div.string  # getting the text inside div
    review_list.append(review)
    print "Review: \n",review,"\n"

size = 1  # 1 item per sublist

# Splitting the list into sublists
review_sub_list = [review_list[i:i+size] for i in range(0, len(review_list), size)]

ws['B1'] = "Facebook Page Reviews crawled by the Python crawler"

for item in review_sub_list:
    ws.append(item)

# Save the file
wb.save("facebook_page_reviews.xlsx")
