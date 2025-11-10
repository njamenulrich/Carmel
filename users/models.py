from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field not set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
    


class Users(AbstractBaseUser, PermissionsMixin):

    roles = (
            ("Admin", "Admin"),
            ("Recruiter", "Recruiter" ),
            ("Job seeker", "Job seeker")
        )

    email = models.EmailField(unique = True)
    name = models.CharField(max_length=255, blank = True, default = "")
    role = models.CharField(max_length=20, choices = roles)
    recovered_on = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
        
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.name
        
    def get_short_name(self):
        return self.name or self.email.split("@")[0]
        


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to= "profiles",
        default= "avatar.jpg"
    )
    location = models.CharField(max_length=255, blank=True, default="")
    phone = models.IntegerField(blank=True, null=True)


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"