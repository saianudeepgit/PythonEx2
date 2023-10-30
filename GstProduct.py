import os
class Goods:
    def __init__(self, name, price, category, gst_rate):
        self.name = name
        self.price = price
        self.category = category
        self.gst_rate = gst_rate
    def calculate_gst(self):
        gst_amount = self.price * (self.gst_rate / 100)
        return gst_amount

def create_goods_info_file(goods_list):
    with open("goodsInfo.txt", "w") as f:
        for goods in goods_list:
            f.write(f"{goods.name},{goods.price},{goods.category},{goods.gst_rate}\n")

def read_goods_info_file(category):
    goods_list = []
    with open("goodsInfo.txt", "r") as f:
        for line in f:
            goods_info = line.split(",")
            goods = Goods(goods_info[0], float(goods_info[1]), goods_info[2], float(goods_info[3]))
            goods_list.append(goods)

    return [goods for goods in goods_list if goods.category == category]

def calculate_gst_for_category(goods_list):
    gst_paid = 0
    for goods in goods_list:
        gst_paid += goods.calculate_gst()
    return gst_paid

def main():
    #goodObj1 = Goods("Mobile", 10000, "Electronics", 18)
    goods_list = [
        Goods("Mobile", 10000, "Electronics", 18),
        Goods("Television", 50000, "Electronics", 18),
        Goods("Fridge", 30000, "Electronics", 18),
        Goods("Book", 500, "Books", 5),
        Goods("Pen", 100, "Stationery", 12),
    ]

    create_goods_info_file(goods_list)

    electronics_goods = read_goods_info_file("Electronics")
    print("GST paid for Electronics goods:", calculate_gst_for_category(electronics_goods))
    
    books_goods = read_goods_info_file("Books")
    print("GST paid for Books goods:", calculate_gst_for_category(books_goods))

    stationery_goods = read_goods_info_file("Stationery")
    print("GST paid for Stationery goods:", calculate_gst_for_category(stationery_goods))

if __name__ == "__main__":
    main()