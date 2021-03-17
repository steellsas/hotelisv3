from decimal import Decimal
from django.conf import settings
from rooms.models import Room

class Cart(object):

    # DAY = start_day - end_day

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, room, start_day, end_day) :
        """
        Add a product to the cart or update its quantity.
        """
        room_id = str(room.id)
        if room_id not in self.cart:
            self.cart[room_id] = {'start_day': start_day ,'end_day':end_day , 'price': str(room.price) }

        self.save()

    def save(self):
            # mark the session as "modified" to make sure it gets saved
            self.session.modified = True


    def remove(self, product):
        """
        Remove a product from the cart.
        """
        room_id = str(room.id)
        if room_id in self.cart:
            del self.cart[room_id]
            self.save()


    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        room_ids = self.cart.keys()
        # get the product objects and add them to the cart
        rooms = Room.objects.filter(id__in=room_ids)

        cart = self.cart.copy()
        for room in rooms:
            cart[str(room.id)]['room'] = room

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * (item['Start_day'] -item['end_day'])
            yield item


    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum((item['start_day'] -item['end_day']) for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * (item['start_day'] -item['end_day']) for item in self.cart.values())


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()