from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name", default="food")
    quantity = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Quantity")
    unit = models.CharField(max_length=6, verbose_name="Unit", default="grams")
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Price")
    
    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    title = models.CharField(max_length=20, verbose_name="Title", default="Best food")
    price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Price")
    
    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    quantity = models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Quantity")
    menuitem = models.ForeignKey("MenuItem", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.quantity) + " " + str(self.ingredient) + " - " + str(self.menuitem)
    

class Purchase(models.Model):
    menuitem = models.ForeignKey("MenuItem", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return str(self.menuitem) + " " + str(self.timestamp)