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
    offers = []
    page_url = 'https://www.ceneo.pl/71793084'
    time = helper.return_time()
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    container =  soup.find_all("div", "product-offer__container")
    

    
    for container_row in container:
        id = helper.return_uuid()
        logos.append(container_row['data-shopurl'])
        prices.append(container_row['data-price'])
        db.create_offer(conn, (id.hex, logos[-1], prices[-1], time))
        offers.append([id.hex, logos[-1], prices[-1], time])

    today_result = min(offers, key=lambda x: x[2] )
    db.today_best_offer(conn,today_result)
    best_offer = db.filter_best_offer(conn)
    print(best_offer)
    # whatsapp.send_message(f'Witaj Marcin!👋\n\nW dniu {best_offer[0][3]} 📅\nZnalazlem oferte dla: {page_url}  \nCena: {best_offer[0][0]}PLN 🏷️  \nFirma: {best_offer[0][1]} 🛒\n')
    whatsapp.send_message("Witaj Marcin!👋\n\n📅 Termin:{3}\n🏷️ Najlepsza oferta w: {1} \nCena: {2} PLN \n🛒 Firma:{3} \n\n Najlepsza byla {7}: W cenie {6} Na: {5}\t \n".format(*today_result,*best_offer[0]))

    # print(logos, prices)



if __name__ == '__main__':
    main()
    