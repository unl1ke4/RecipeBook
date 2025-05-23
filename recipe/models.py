from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __iter__(self):
        # Припустимо, ви хочете ітеруватись по символах назви
        return iter(self.name)

