from django.contrib import admin

# Register your models here.
from .models import (
    Product,
    HomepageProductFruits,
    HomepageProductVegetable,
    FreshFruit,
    SomeCoolOfferfruits,
    TopDealsTodayfruits,
    FreshVegetables,
    SomeCoolOffervegetables,
    TopDealsTodayvegetables,
    DealsWeek,
    BigPackBiggerDiscount,
    Combos,
    The30RsCorner,
)


# class FruitsAdmin(admin.ModelAdmin):
#     list_display = ("product_name", "category", "per_off", "pub_date")


class HomepageProdAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "pub_date")


# fresh fruits page
class FreshFruitAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "pub_date")


class SomeCoolOfferfruitsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "per_off", "pub_date")


class topdealsfruitsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "per_off", "pub_date")


#  fresh vegetables page
class FreshVegetablesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "pub_date")


class SomeCoolOffervegetablesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "per_off", "pub_date")


class topdealsvegetablesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "per_off", "pub_date")


class DealsWeekAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "pub_date")


class BigPackBiggerDiscountAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "per_off", "pub_date")


class CombosAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "per_off", "pub_date")


class The30RsCornerAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "pub_date")


# Registered Model in Database

admin.site.register(Product)
admin.site.register(HomepageProductFruits, HomepageProdAdmin)

admin.site.register(HomepageProductVegetable, HomepageProdAdmin)

admin.site.register(FreshFruit, FreshFruitAdmin)
admin.site.register(SomeCoolOfferfruits, SomeCoolOfferfruitsAdmin)
admin.site.register(TopDealsTodayfruits, topdealsfruitsAdmin)

admin.site.register(FreshVegetables, FreshVegetablesAdmin)
admin.site.register(SomeCoolOffervegetables, SomeCoolOffervegetablesAdmin)
admin.site.register(TopDealsTodayvegetables, topdealsvegetablesAdmin)

admin.site.register(DealsWeek, DealsWeekAdmin)

admin.site.register(BigPackBiggerDiscount, BigPackBiggerDiscountAdmin)
admin.site.register(Combos, CombosAdmin)
admin.site.register(The30RsCorner, The30RsCornerAdmin)
