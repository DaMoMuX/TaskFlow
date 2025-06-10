from django.db import models

# Create your models here.
class StatusEnum(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'

class Category(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        
        def __str__(self):
                return self.name
        
        class Meta:
                verbose_name_plural = "Categories"

class Task(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        due_date = models.DateField()
        status = models.CharField(max_length=20, choices=StatusEnum.choices, default=StatusEnum.PENDING)
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

        def __str__(self):
                return self.title


