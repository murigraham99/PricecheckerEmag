from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "trafficboutiquepr@gmail.com"
password = "ouuwgislwmtbyalh"

target = 4500


product_html = "https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-128gb-5g-space-black-mpxv3rx-a/pd/DQ7Y4LMBM/?X-Search-Id=0e7eb749d8137d70cc2a&X-Product-Id=101075747&X-Search-Page=1&X-Search-Position=26&X-Section=search&X-MB=0&X-Search-Action=view"
content = requests.get(product_html)
soup = BeautifulSoup(content.text, "html.parser")

price_raw = soup.find(name="p", class_="product-new-price").getText()

title = soup.find (name= "h1", class_="page-title").getText().strip()

print(title)

price = float(price_raw[0:8].replace(".","").replace(",", "."))

print(price)

if price <= target:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="robertomuresan1999@gmail.com",
                            msg=f"Subject: Iphone 14 PRO a atins pretul dorit! \n\n {title} a atin pretul de {target}. \n\n Link: {product_html}")
        print("Mail sent successfully!")