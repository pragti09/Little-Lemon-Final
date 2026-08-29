from django.db import models

# Create your models here.
class Menu(models.Model):
    id= models.AutoField( primary_key=True)
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Inventory=models.SmallIntegerField()
    
    def __str__(self):
        return f"{self.Title} : {str(self.Price)}"
    
class Bookings(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateField()