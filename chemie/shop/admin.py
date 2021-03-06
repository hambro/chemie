from django.contrib import admin

from .models import Item, Category, Order, OrderItem, RefillReceipt, HappyHour


class RefillReceiptAdmin(admin.ModelAdmin):
    list_display = ["provider", "receiver", "amount"]
    search_fields = ["provider"]
    list_display_links = None

    class Meta:
        model = RefillReceipt

    def has_delete_permission(self, request, obj=None):
        return False


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_filter = ["name", "price"]
    search_fields = ["name"]

    class Meta:
        model = Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Category


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["item", "quantity", "total_price", "get_order"]
    search_fields = ["item"]
    list_display_links = None

    class Meta:
        model = OrderItem

    def get_order(self, obj):
        return obj.order.all()[0]

    get_order.short_description = "Ordre"

    def has_delete_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "buyer", "created", "get_price"]
    search_fields = ["id", "buyer"]
    list_display_links = None

    class Meta:
        model = Order

    def get_price(self, obj):
        return obj.get_total_price()

    def has_delete_permission(self, request, obj=None):
        return False

    get_price.short_description = "Totalpris"


class HappyHourAdmin(admin.ModelAdmin):
    list_display = ["id", "provider", "created"]
    search_fields = ["provider"]

    class Meta:
        model = HappyHour


admin.site.register(RefillReceipt, RefillReceiptAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(HappyHour, HappyHourAdmin)
