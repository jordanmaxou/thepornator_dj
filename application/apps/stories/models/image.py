from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to="img/stories")
    blog = models.ForeignKey("Story", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.file.url
