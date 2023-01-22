from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, name):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, name):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    is_driver = models.BooleanField(default=False)
    email = models.EmailField(
         verbose_name='email address',
         max_length=255,
         unique=True,
     )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


class Car(models.Model):
    #image = models.ImageField(upload_to='car_image/%Y/%m/%d', blank=True, null=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    price = models.IntegerField()
    seats = models.IntegerField(default=4)
    large_suitcases = models.IntegerField(default=1)
    carry_on_bags = models.IntegerField(default=2)
    driver = models.ForeignKey(User, to_field='email', null=False, on_delete=models.CASCADE, db_column='driver')
    

class Booking(models.Model):
    user = models.ForeignKey(User, to_field='email', null=False, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, to_field='name', null=False, on_delete=models.CASCADE)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    