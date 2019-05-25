from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    LIBRARIAN_SENIORITY = (
        ('s', 'Senior'),
        ('j', 'Junior'),
    )

    seniority = models.CharField(
        max_length=1,
        choices=LIBRARIAN_SENIORITY,
        blank=True,
        default='j',
        help_text='Seniority level')

    def __str__(self):
        return f"{self.user}"
