from django.db import models
from users.models import CustomUser as User

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    document = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            return f"{self.text[:50]}..."
