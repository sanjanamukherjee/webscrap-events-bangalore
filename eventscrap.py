
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

my_url= "https://www.eventbrite.com/d/india--bengaluru/events/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"eds-media-card-content__content__principal"})

filename= "events.csv"
f = open(filename,"w")

headers = "event, day, date, time, location, price\n"

f.write(headers)


for container in containers :
	
	title_container= container.a.div.div
	event = title_container.text

	another_container = container.findAll("div",{"class":"eds-media-card-content__sub-content"})
	date = another_container[0].div.text

	place_container= container.findAll("div",{"class":"eds-media-card-content__sub-content-cropped"})
	location = place_container[0].div.text

	price_container= place_container[0].findAll("div",{"class":"eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1"})

	if len(price_container) > 0:
		price= price_container[1].text
	else: price= "unknown"

	print("event" + event)
	print("date" + date)
	print("location" + location)
	print("price" + price)

	f.write(event + "," + date + "," + location.replace(",","|") + "," + price + "\n")

f.close()
