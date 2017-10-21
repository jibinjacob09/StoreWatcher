from sw import StoreItems

computer_parts = dict()

computer_parts["cpu"] = StoreItems("AMD RYZEN 1600", 298.99,
                 Amazon="https://www.amazon.ca/AMD-Ryzen-1600X-Processor-YD160XBCAEWOF/dp/B06XKWT7GD/ref=sr_1_2?ie=UTF8&qid=1507337664&sr=8-2&keywords=amd+ryzen+1600",
                 NewEgg="https://www.newegg.ca/Product/Product.aspx?Item=N82E16819113435",
                 CanadaComps="http://www.canadacomputers.com/product_info.php?cPath=4_1210_64&item_id=105321")

computer_parts["mother_board"] = StoreItems("ASRock AB350M Pro4 AM4 AMD Promontory B350", 119.00,
                          NewEgg="https://www.newegg.ca/Product/Product.aspx?item=N82E16813157762",
                          CanadaComps="http://www.canadacomputers.com/product_info.php?cPath=26_1207_1205_1505&item_id=104786"
                          )
computer_parts["graphics_card"] = StoreItems("Asus GeForce GTX 1080", 699.99,
                           NewEgg="https://www.newegg.ca/Product/Product.aspx?Item=N82E16814126110&cm_re=Asus_-_GeForce_GTX_1080_8GB_TURBO_Video_Card-_-14-126-110-_-Product",
                         )
computer_parts["case"] = StoreItems("Genome II", 299.99,
                  NewEgg="https://www.newegg.ca/Product/Product.aspx?Item=N82E16811853048&cm_re=Genome-_-11-853-048-_-Product",
                  )
computer_parts["psu"] = StoreItems("Seasonic G series", 94.00,
                 NewEgg="https://www.newegg.ca/Product/Product.aspx?Item=N82E16817151119&cm_re=SeaSonic_-_G_550W_80%2b_Gold_Certified_Semi-Modular_ATX_Power_Supply-_-17-151-119-_-Product",
                 )

for parts in computer_parts.keys():
    print(computer_parts[parts].get_sale_prices())