from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Job(models.Model):
    creator = models.ForeignKey(User, blank = True, null = True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    cost = models.IntegerField()
    location = models.TextField()
    DEPARTMENT_CHOICES = (
        ('CORP', 'Corporate'),
        ('ACCT', 'Accounting'),
        ('OPER', 'Operations'),
    )
    department = models.CharField(
        max_length=4,
        choices=DEPARTMENT_CHOICES,
        default='CORP',
    )


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
