from django.db import models


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=55)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = "Manufacture"
        verbose_name_plural = "Manufactures"


class Users(models.Model):
    full_name = models.CharField(max_length=70)
    user_name = models.CharField(max_length=70, unique=True)
    # liked_cars = models.ManyToManyField('Cars')
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(unique=True, max_length=30)
    user_image = models.FileField(upload_to="users_images")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)
    car_year = models.IntegerField()
    car_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    car_description = models.TextField()
    car_number = models.CharField(max_length=8, unique=True)
    car_color = models.CharField(max_length=50)
    car_price = models.DecimalField(decimal_places=3, max_digits=255)
    made_in = models.CharField(max_length=30)
    car_image = models.FileField(upload_to="cars_images")
    car_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars "
