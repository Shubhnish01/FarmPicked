from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class HomepageProductFruits(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class HomepageProductVegetable(models.Model):
    vege_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class FreshFruit(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class SomeCoolOfferfruits(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class TopDealsTodayfruits(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class FreshVegetables(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class SomeCoolOffervegetables(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class TopDealsTodayvegetables(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class DealsWeek(models.Model):
    dealweek_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class BigPackBiggerDiscount(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    per_off = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Combos(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    per_off = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class The30RsCorner(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="shop/images", default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
