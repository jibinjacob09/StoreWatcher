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
        return float(sale_price.strip("'"))

    def get_sale_price_in_canadacomps(self):
        bs = BeautifulSoup(self.get_store_page_html(), "html.parser")
        sale_price = bs.find("p", attrs={"itemprop": "price"}).next
        return float(sale_price.replace("$", "").strip())

class StoreItems:

    def __init__(self, name, base_price, **kwargs):
        self.name = name
        self.base_price = base_price
        self.stores = dict()

        for key, value in kwargs.items():
            self.stores[key] = (Store(key, value))

    def get_sale_prices(self):
        sale_info = list()
        for store in self.stores.values():
            curr_price = self.base_price
            if "NewEgg" == store.name:
                #curr_price = store.get_sale_price_in_newegg()
                pass
            elif "CanadaComps" == store.name:
                curr_price = store.get_sale_price_in_canadacomps()

            if self._is_on_sale(curr_price):
                sale_info.append("{0} on sale @ {1}, ${2} instead of ${3}".format(self.name, store.name, curr_price,
                                                                                  self.base_price))
        return sale_info

    def _is_on_sale(self, price):
        if price < self.base_price:
            return True
        else:
            return False

