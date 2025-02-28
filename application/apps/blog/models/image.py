from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to="img/blog")
    blog = models.ForeignKey("Blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.file.url
