from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.search}"  # change 'search object(1)' with it's original name in admin side

    class Meta:
        """It acts as a configuration class and keeps the configuration data in one place and
            defines such things as available permissions, associated database table name,
         whether the model is abstract or not, singular and plural versions of the name etc."""
        verbose_name_plural = 'Searches'
