from django.contrib import admin

from .models import Locker, LockerUser, Ownership, LockerToken


class LockerAdmin(admin.ModelAdmin):
    search_fields = ["number"]

    # list_display_links = None

    class Meta:
        model = Locker
        ordering = ['number']


class LockerUserAdmin(admin.ModelAdmin):
    list_display = ["email"]
    list_filter = ["created"]
    search_fields = ["email"]
    list_display_links = None

    class Meta:
        model = LockerUser


class OwnershipAdmin(admin.ModelAdmin):
    list_display = ["get_locker_number", "get_user"]

    def get_user(self, obj):
        return obj.user.email

    get_user.short_description = 'User'
    get_user.admin_order_field = 'locker__email'

    def get_locker_number(self, obj):
        return obj.locker.number

    get_locker_number.short_description = "skapnummer"
    get_locker_number.admin_order_field = "number"

    class Meta:
        model = Ownership


class ConfirmationAdmin(admin.ModelAdmin):

    class Meta:
        model = LockerToken


admin.site.register(LockerToken, ConfirmationAdmin)
admin.site.register(Locker, LockerAdmin)
admin.site.register(LockerUser, LockerUserAdmin)
admin.site.register(Ownership, OwnershipAdmin)
