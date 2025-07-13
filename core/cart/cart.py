class CartSession:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault('cart', {
            "items": [],
            "total_price": 0,
            "total_items": 0,
        })
        self.session['cart'] = self.cart
        self.save()

    def save(self):
        self.session.modified = True

    def remove_product(self, product_id):
        self.cart["items"] = [
            item for item in self.cart["items"] if str(item["product_id"]) != str(product_id)
        ]
        self.save()

    def update_quantity(self, product_id, quantity):
        for item in self.cart["items"]:
            if str(item["product_id"]) == str(product_id):
                item["quantity"] = int(quantity)
                break
        self.save()

    def add_product(self, product_id, quantity=1):
        for item in self.cart['items']:
            if str(item['product_id']) == str(product_id):
                item['quantity'] += int(quantity)
                break
        else:
            self.cart['items'].append({
                "product_id": str(product_id),
                "quantity": int(quantity),
            })
        self.save()

    def get_products(self):
        return self.cart['items']

    def get_total_quantity(self):
        return sum(item["quantity"] for item in self.cart["items"])

    def sync_cart_items_from_db(self):
        pass
    def merge_session_cart_in_db(self):
        pass
# ======================================================================================================================