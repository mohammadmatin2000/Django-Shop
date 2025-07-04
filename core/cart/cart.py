class CartSession:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {
            "items": [],
            "total_price": 0,
            "total_items": 0,
        })
        self.session['cart'] = self.cart
        self.session.modified = True
        self.add_product(request)
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

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
# ======================================================================================================================