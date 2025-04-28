from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser , Group, Permission 
from django.db import models
import uuid



class Manager(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    last_update = models.DateTimeField( auto_now= True)
    created_at = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField( max_length= 128)
    profile_picture = models.ImageField( upload_to='profile_pictures/', null= True, blank= True)

    groups = models.ManyToManyField(
        Group,
        related_name="manager_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="manager_permissions",
        blank=True
    )

    class Meta:
        db_table = "managers" # like default but i felt like adding it
        # unique_together = ('first_name', 'last_name') # i should think about this constraint
        verbose_name = _("Manager")
        verbose_name_plural = _("Managers")


class Driver(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    last_update = models.DateTimeField( auto_now= True)
    created_at = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField( max_length=128)
    profile_picture = models.ImageField( upload_to='profile_pictures/', null= True, blank= True)
    manager = models.ForeignKey( Manager, related_name='drivers', on_delete=models.CASCADE)

    groups = models.ManyToManyField(
        Group,
        related_name="driver_set",
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="driver_permissions",
        blank=True
    )


    class Meta:
        db_table = "drivers"
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")