from bs4 import BeautifulSoup
import requests
from art_crs import logo

def get_rate(in_currency , out_currency):
    url =f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"

    # accessing the entire source code of the page
    content = requests.get(url).text

    # converitng the entire source code into a beautifulsoup object
    soup = BeautifulSoup(content, 'html.parser')

    # get the desired value from the code of the html page in a text form (string)
    rate = soup.find("span", class_='ccOutputRslt').get_text()

    # converting the string value into a float (55.0 INR -> 55.0)
    value_float = float(rate[:-4])

    return f"\n1 {in_currency} is currently equal to {value_float} {out_currency}\n"

print(logo)
input_c1 = input("\nPlease enter the currency you would like to compare the current currency rate to \n").upper()
input_c2 = input(f"Please enter the currency you would like to compare to {input_c1}\n").upper()


currency_rate = get_rate(input_c1 , input_c2)

print(currency_rate)

# To Do: make a method so that invalid currencies can be identified.