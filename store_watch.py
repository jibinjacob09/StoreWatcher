from sw import StoreItems

cpu = StoreItems("AMD RYZEN 1600", 298.99,
                 Amazon="https://www.amazon.ca/AMD-Ryzen-1600X-Processor-YD160XBCAEWOF/dp/B06XKWT7GD/ref=sr_1_2?ie=UTF8&qid=1507337664&sr=8-2&keywords=amd+ryzen+1600",
                 NewEgg="https://www.newegg.ca/Product/Product.aspx?Item=N82E16819113435",
                 CanadaComps="http://www.canadacomputers.com/product_info.php?cPath=4_1210_64&item_id=105321")
print(cpu.get_sale_prices())