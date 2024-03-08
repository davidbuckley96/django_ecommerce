from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be filled')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default='placeholder_product.jpg', null=True, blank=True)
    digital = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    discount = models.BooleanField(default=False, null=True, blank=True)
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-date_modified']

    @property
    def discount_price(self):
        if self.discount:
            amount = self.price * self.discount_percent / 100
            total = self.price - amount
            return total

    def __str__(self):
        return self.name
    

class Review(models.Model):
  user = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now=True)
  body = models.TextField()
  recommend = models.BooleanField(default=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total_value for item in order_items])
        return total

    @property
    def get_cart_quantity(self):
        order_items = self.orderitem_set.all()
        total = sum(item.quantity for item in order_items)
        return total

    @property
    def shipping(self):
        shipping = False
        order_items = self.orderitem_set.all()
        for item in order_items:
            if item.product.digital is False:
                shipping = True
        return shipping

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_value(self):
        if self.product.discount:
            total = round(self.product.discount_price, 2) * self.quantity
        else:
            total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=255, unique=False, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
