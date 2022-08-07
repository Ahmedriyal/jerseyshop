from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClubJerseyDetails(models.Model):
    title = models.CharField(max_length=150)

    Fan_Version = 'Fan Version'
    Player_Version = 'Player Version'

    type_choices = [
        (Fan_Version, 'Fan Version'),
        (Player_Version, 'Player Version'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    added_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def small_image1URL(self):
        try:
            url = self.small_image1.url
        except:
            url = ''
        return url

    @property
    def small_image2URL(self):
        try:
            url = self.small_image2.url
        except:
            url = ''
        return url

    @property
    def small_image3URL(self):
        try:
            url = self.small_image3.url
        except:
            url = ''
        return url

    @property
    def small_image4URL(self):
        try:
            url = self.small_image4.url
        except:
            url = ''
        return url



class NTJerseyDetails(models.Model):
    title = models.CharField(max_length=150)

    Fan_Version = 'Fan Version'
    Player_Version = 'Player Version'

    type_choices = [
        (Fan_Version, 'Fan Version'),
        (Player_Version, 'Player Version'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    added_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def small_image1URL(self):
        try:
            url = self.small_image1.url
        except:
            url = ''
        return url

    @property
    def small_image2URL(self):
        try:
            url = self.small_image2.url
        except:
            url = ''
        return url

    @property
    def small_image3URL(self):
        try:
            url = self.small_image3.url
        except:
            url = ''
        return url

    @property
    def small_image4URL(self):
        try:
            url = self.small_image4.url
        except:
            url = ''
        return url


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     email = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    club_jersey = models.ForeignKey(ClubJerseyDetails, on_delete=models.SET_NULL, null=True, blank=True)
    national_jersey = models.ForeignKey(NTJerseyDetails, on_delete=models.SET_NULL, null=True, blank=True)

    Select_Size = 'Select Size'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'

    size_choices = [
        (Select_Size, 'Select Size'),
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
        (XXL, 'XXL'),
    ]
    size = models.CharField(max_length=20, choices=size_choices, default=Select_Size)
    quantity = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.order.id)

    @property
    def get_total(self):
        if self.club_jersey_id is not None:
            total = self.club_jersey.price * self.quantity
            return total

        elif self.national_jersey_id is not None:
            total = self.national_jersey.price * self.quantity
            return total
        else:
            return 'None'


class ShippingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    mobileNo = models.CharField(max_length=100, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.order.id)

