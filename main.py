import requests
from bs4 import BeautifulSoup
import smtplib

LOW_PRICE = 2500

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,ta;q=0.8",
}

# reading amazon product price
response = requests.get(url="https://www.amazon.in/MuscleBlaze-Performance-Clinically-Absorption-Certified/dp/B0BPCR7K7F?ref_=Oct_DLandingS_M_9960e767_3",headers=header)
print(response.raise_for_status())
# print(response.text)
webhtml = response.content


# creating soup
soup = BeautifulSoup(webhtml,"lxml")
# print(soup.prettify())
price = int(soup.find(class_="a-price-whole").get_text().replace(",","").replace(".",""))
print(price)

msg = f"The Current price of Iphone 13 is {price}, which is lower than your least price {LOW_PRICE}, So grab the deal!!!"
if price < LOW_PRICE:
    username = "Your email"
    password = "Your Email APP password"
    with smtplib.SMTP("smtp.gmail.com", port=587) as con:
        con.starttls()
        con.login(user=username, password=password)
        con.sendmail(from_addr=username,
                     to_addrs="To Email",
                     msg=f"Subject: Product Price is below low price!!\n\nHi,\n{msg}")
        print("Low Price Alert Mail Sent")
