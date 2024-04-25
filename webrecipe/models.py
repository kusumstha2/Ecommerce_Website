from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user_id}. {self.first_name} {self.last_name}"


class Categories(models.Model):
   
    category = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.category}. {self.category}"

class Product(models.Model):
   
    product = models.CharField(max_length=255)
    description = models.TextField()
    image=models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
   

    def __str__(self):
        return  f"{self.product}"
    
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]

    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Order ({self.order_date})"

class OrderItem(models.Model):
   
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item {self.order}"

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart  {self.product}"





class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment {self.payment_id} for Order {self.order_id}"

