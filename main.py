import requests
from bs4 import BeautifulSoup
from dbConnect import DataBaseHandler
import uuid
from datetime import date

from whatsapp import WhatsappHandler


def main():
    db = DataBaseHandler()
    whatsapp = WhatsappHandler()
    # db.conn
    gather_date(db, whatsapp, conn=db.conn)

def gather_date(db,whatsapp, conn):
    prices = []
    logos = []
    time = date.today().strftime("%B %d, %Y %I:%M%p")
    page = requests.get('https://www.ceneo.pl/71793084')
    soup = BeautifulSoup(page.content, "html.parser")
    container =  soup.find_all("div", "product-offer__container")
    

    
    for container_row in container:
        id = uuid.uuid4()
        logos.append(container_row['data-shopurl'])
        prices.append(container_row['data-price'])
        db.create_offer(conn, (id.hex, logos[-1], prices[-1], time))
    
    best_offer = db.filter_best_offer(conn)
    whatsapp.send_message(' '.join(map(str,best_offer)))

    print(logos, prices)
# div class product-offer__container
if __name__ == '__main__':
    main()
    