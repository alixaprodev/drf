from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group
from django.db import models
from .managers import CustomUserManager
        
# Define the custom User model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define related names for groups and user permissions
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'
        
    

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=200, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    
# How to query all orders of a User along wth products
class Order(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order :{self.id} Paced by :{self.user.username}'
    
class Address(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE )
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.address} {self.city} {self.country}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in Order #{self.order.id}'
    

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'Cart for {self.user.username}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in Cart for {self.cart.user.username}'
    
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    rating= models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class SiteUser(models.Model):
    name = models.CharField(max_length=32)
 