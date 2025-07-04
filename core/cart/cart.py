class CartSession:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault('cart', {
            "items": [],
            "total_price": 0,
            "total_items": 0,
        })
        self.session['cart'] = self.cart
        self.session.modified = True
        self.save()
    def add_product(self, product_id):
        for item in self.cart['items']:
            item['quantity'] += 1
            break
        else:
            new_item={
                "product_id": product_id,
                "quantity": 1,
            }
            self.cart['items'].append(new_item)
        self.save()
    def get_add_product(self):
        return self.cart['items']


    def save(self):
        self.session.modified = True
# ======================================================================================================================