from typing import Container
import requests
from bs4 import BeautifulSoup
from dbConnect import DataBaseHandler
import uuid
import random
def main():
    db = DataBaseHandler()
    # db.conn
    gather_date(db, conn=db.conn)

def gather_date(db, conn):
    prices = []
    logos = []

    page = requests.get('https://www.ceneo.pl/71793084')
    soup = BeautifulSoup(page.content, "html.parser")
    container =  soup.find_all("div", "product-offer__container")
    

    
    for container_row in container:
        id = uuid.uuid4()
        logos.append(container_row['data-shopurl'])
        prices.append(container_row['data-price'])
        db.create_offer(conn, (id.hex, logos[-1],prices[-1]))
    


    print(logos, prices)
# div class product-offer__container
if __name__ == '__main__':
    main()
    