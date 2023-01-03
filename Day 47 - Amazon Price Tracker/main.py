import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

URL = "https://www.amazon.com/Razer-BlackShark-Gaming-Headset-Detachable/dp/B086PKMZ1Q/ref=sxin_25_ac_d_mf_brs?ac_md=4-3-UmF6ZXI%3D-ac_d_mf_brs_brs&content-id=amzn1.sym.1d3b962f-00ed-4296-9689-8bc4c83edc14%3Aamzn1.sym.1d3b962f-00ed-4296-9689-8bc4c83edc14&cv_ct_cx=gaming%2Bheadsets&keywords=gaming%2Bheadsets&pd_rd_i=B086PKMZ1Q&pd_rd_r=a1a891f9-1b03-449c-a3bf-65e178622c88&pd_rd_w=syB1G&pd_rd_wg=x4RWm&pf_rd_p=1d3b962f-00ed-4296-9689-8bc4c83edc14&pf_rd_r=T9VNW3ABS6CCYR6DYTH9&qid=1672754322&sr=1-3-df9394e9-2684-45bf-8eee-ec356375596d&th=1"

url_headers = {
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers= url_headers)
product_page = response.text

soup = BeautifulSoup(product_page, "html.parser")

product_name = soup.find(name = "span", id = "productTitle").get_text().strip()

product_price_whole = soup.find(name= "span", class_ = "a-price-whole").getText()
product_price_fraction = soup.find(name= "span", class_ = "a-price-fraction").getText()

product_price = float(product_price_whole + product_price_fraction)

if product_price <= 100.00:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD,)
        connection.sendmail(
            from_addr= MY_EMAIL, 
            to_addrs= MY_EMAIL, 
            msg= f"Subject: Amazon Price Alert\n\n{product_name} is now ${product_price}\n{URL}"
            )