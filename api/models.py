from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


SEX_CHOICES = (
    ('F', 'Mujer',),
    ('M', 'Hombre',),
    ('E', 'No binario',),
)

def get_opposed_sex(sex):
    return 'M' if sex == 'F' else 'F'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True, db_index=True)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    picture1 = models.FileField(blank=False)
    picture2 = models.FileField(blank=True)
    picture3 = models.FileField(blank=True)
    picture4 = models.FileField(blank=True)
    picture5 = models.FileField(blank=True)
    picture6 = models.FileField(blank=True)

    about_me = models.CharField(max_length=150, default='#BuscandoMiTigreOTigresa')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, db_index=True)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)], null=True)

    preferred_sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    preferred_age_min = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)], null=True)
    preferred_age_max = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)], null=True)
    preferred_radius = models.IntegerField(default=5, help_text="en km")

    location_lat = models.FloatField(max_length=40, null=True)
    location_long = models.FloatField(max_length=40, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def homo(self):
        return self.preferred_sex == self.sex

    @property
    def get_opposed_sex(self):
        return get_opposed_sex(self.sex)

    def __str__(self):
        return self.email