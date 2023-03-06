from django.db import models

# Create your models here.

class administrators(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    ROL = (
        ("administrator", "administrator"),
        ("super_administrator", "super_administrator")
    )

    rol = models.CharField(max_length=20,
                    choices=ROL,
                    default="administrator")
    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("can_create",               "create"),
			("can_read",                    "read"),
			("can_update",                  "update"),
			("can_delete",                  "delete"),


		)
    def __str__(self):
        return '{}'.format(self.name)
	

class customer(models.Model):
	name = models.CharField(max_length=30)
	paternal_surname = models.CharField(max_length=30)
	email  = models.EmailField(max_length=30)

	def __str__(self):
		return '{}'.format(self.id)

class payments_customer(models.Model):
	amount = models.DecimalField(max_digits = 5,
                         decimal_places = 2)
	customer_id = models.ForeignKey(
        "customer", on_delete=models.CASCADE)
	product_name  = models.CharField(max_length=50)
	quantity = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.product_name)