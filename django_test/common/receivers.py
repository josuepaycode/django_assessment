from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission

from customers.models import Customer
from payments.models import Payment

def assign_admin_permissions(sender, instance: User, **kwargs):
    if instance.is_staff and instance.user_permissions.all().count() == 0:
        content_type = ContentType.objects.get_for_model(Payment)
        permissions = Permission.objects.filter(content_type=content_type)

        for perm in permissions:
            if perm.codename == "view_payment":
                print(f"New permission added: {perm.codename}")
                print(perm)
                instance.user_permissions.add(perm)

        content_type = ContentType.objects.get_for_model(Customer)
        permissions = Permission.objects.filter(content_type=content_type)

        for perm in permissions:
            if perm.codename == "view_customer":
                print(f"New permission added: {perm.codename}")
                print(perm)
                instance.user_permissions.add(perm)
