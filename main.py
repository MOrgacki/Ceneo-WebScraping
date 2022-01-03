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
    page_url = 'https://www.ceneo.pl/71793084'
    time = date.today().strftime("%d %B %Y")
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    container =  soup.find_all("div", "product-offer__container")
    

    
    for container_row in container:
        id = uuid.uuid4()
        logos.append(container_row['data-shopurl'])
        prices.append(container_row['data-price'])
        db.create_offer(conn, (id.hex, logos[-1], prices[-1], time))
    
    best_offer = db.filter_best_offer(conn)
    whatsapp.send_message(f'Witaj Marcin!👋\n\nW dniu {best_offer[0][3]} 📅\nZnalazlem oferte dla: {page_url}  \nCena: {best_offer[0][0]}PLN 🏷️  \nFirma: {best_offer[0][1]} 🛒\n')
    # whatsapp.send_message('Witaj Marcin!👋\n\nW dniu {3} 📅\nZnalazlem oferte dla: {page_url}  \nCena: {0}PLN 🏷️  \nFirma: {1} 🛒\n'.format(*best_offer[0][0]))

    print(logos, prices)



if __name__ == '__main__':
    main()
    