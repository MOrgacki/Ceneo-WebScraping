import requests
from bs4 import BeautifulSoup
from dbConnect import DataBaseHandler

# TODO: Rozkminiac jak filtrowac oferty czy odrazu czy nie
from helpers import Helpers

from whatsapp import WhatsappHandler

def main():
    db = DataBaseHandler()
    whatsapp = WhatsappHandler()
    helper = Helpers()

    # db.conn
    gather_date(db, whatsapp, helper, conn=db.conn)

def gather_date(db: DataBaseHandler, whatsapp: WhatsappHandler, helper: Helpers, conn):
    prices = []
    logos = []
    page_url = 'https://www.ceneo.pl/71793084'
    time = helper.return_time()
    print(time)
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    container =  soup.find_all("div", "product-offer__container")
    

    
    for container_row in container:
        id = helper.return_uuid()
        logos.append(container_row['data-shopurl'])
        prices.append(container_row['data-price'])
        db.create_offer(conn, (id.hex, logos[-1], prices[-1], time))

    db.store_offer(conn)
    # whatsapp.send_message(f'Witaj Marcin!👋\n\nW dniu {best_offer[0][3]} 📅\nZnalazlem oferte dla: {page_url}  \nCena: {best_offer[0][0]}PLN 🏷️  \nFirma: {best_offer[0][1]} 🛒\n')
    # whatsapp.send_message('Witaj Marcin!👋\n\nW dniu {3} 📅\nZnalazlem oferte dla: {page_url}  \nCena: {0}PLN 🏷️  \nFirma: {1} 🛒\n'.format(*best_offer[0][0]))

    # print(logos, prices)



if __name__ == '__main__':
    main()
    