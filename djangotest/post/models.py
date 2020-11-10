from django.db import models

class Post(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content, self.created_time
