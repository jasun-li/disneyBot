from bs4 import BeautifulSoup

with open("december.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())

#print(soup.find_all("calendarContainer"))