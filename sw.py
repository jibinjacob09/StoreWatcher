import pycurl
from bs4 import BeautifulSoup
from io import BytesIO


class Store:

    def __init__(self, store_name, store_page_url):
        self.name = store_name
        self.url = store_page_url

    def get_store_page_html(self):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()

        body = buffer.getvalue()
        html = body.decode('iso-8859-1')
        return html

    def get_sale_price_in_newegg(self):
        bs = BeautifulSoup(self.get_store_page_html(), "html.parser")
        start_pos = bs.get_text().find("product_sale_price")
        pos1 = bs.get_text().find("[", start_pos) + len("[")
        pos2 = bs.get_text().find("]", pos1)
        sale_price = bs.get_text()[pos1:pos2]
        try:
            sale_price = float(sale_price.strip("'"))
        except ValueError:
            sale_price = "error"
        return sale_price

    def get_sale_price_in_canadacomps(self):
        bs = BeautifulSoup(self.get_store_page_html(), "html.parser")
        sale_price = bs.find("p", attrs={"itemprop": "price"}).next
        try:
            sale_price = float(sale_price.replace("$", "").strip())
        except ValueError:
            sale_price = "error"
        return sale_price

class StoreItems:

    def __init__(self, name, base_price, **kwargs):
        self.name = name
        self.base_price = base_price
        self.stores = dict()

        for key, value in kwargs.items():
            self.stores[key] = (Store(key, value))

    def get_sale_prices(self):
        sale_lst = list()
        for store in self.stores.values():
            curr_price = self.base_price
            if "NewEgg" == store.name:
                curr_price = store.get_sale_price_in_newegg()
            elif "CanadaComps" == store.name:
                curr_price = store.get_sale_price_in_canadacomps()

            if curr_price == "error" or self._is_on_sale(curr_price):
                sale_lst.append("{0}: ${1}".format(store.name, curr_price))
        if len(sale_lst) > 0:
            sale_info = ("{0}  baseprice=${1}".format(self.name, self.base_price), sale_lst)
        else:
            sale_info = None
        return sale_info

    def _is_on_sale(self, price):
        if price < self.base_price:
            return True
        else:
            return False

