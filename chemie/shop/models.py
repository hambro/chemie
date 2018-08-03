from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategori', unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category", kwargs={'slug': self.slug})


class Item(models.Model):
    name = models.CharField(max_length=40, verbose_name='Varenavn', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=100, verbose_name='Varebeskrivelse', blank=True, null=True, default=None)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='shopitems')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    buyer = models.ForeignKey(User, related_name='orders')

    def get_total_price(self):
        totalprice = 0
        # TODO: This iteration may be invalid. Should be checked. Maybe the attribute 'through' must be used.
        for item in self.items:
            totalprice += item.item.price * item.quantity
        return totalprice

    def __str__(self):
        return self.buyer.username + ' order ' + str(self.id)


class ShoppingCart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        # Method can be used to create items in the Shopcart if it does not already exist
        # and update quantity of item
        item = product.name
        if item not in self.cart:
            price = str(product.price).replace('.', ',')
            self.cart[item] = {'quantity': 0, 'price': price}
        if self.cart[item]['quantity'] + quantity >= 0:
            self.cart[item]['quantity'] += quantity
            self.save()

    def subtract(self, product, quantity=1):
        if quantity > 0:
            self.add(product, -quantity)

    def set(self, product, quantity=1):
        # Used for
        item = product.name
        if item not in self.cart:
            # Necessary conversion to comma for items to use same decimal separator
            price = str(product.price).replace('.', ',')
            self.cart[item] = {'quantity': 0, 'price': price}
        self.cart[item]['quantity'] = quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        item = product.name
        if item in self.cart:
            del self.cart[item]
            self.save()

    def __iter__(self):
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        # Decimal conversion may only be performed if string has dot as decimal separator
        return sum(Decimal(item['price'].replace(',', '.')) * item['quantity'] for item in self.cart.values())

    def buy(self):
        orderitems = []
        for item in self.cart:
            orderitems.append()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


def pre_save_category_receiver(model, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug


pre_save.connect(pre_save_category_receiver, sender=Category)