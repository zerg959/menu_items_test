from django.db import models

class MenuItem(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Название'
        )
    url = models.CharField(
        max_length=255, blank=True, 
        null=True, verbose_name='URL'
        )
    named_url = models.CharField(
        max_length=255, blank=True, 
        null=True, verbose_name='named URL'
        )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name='children',
        verbose_name='Родитель'
        )
    menu_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Название меню'
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            from django.urls import reverse
            return reverse(self.named_url)
        return self.url

    def is_active(self, request_path):
        if request_path == self.get_absolute_url():
            return True
        for child in self.children.all():
            if child.is_active(request_path):
                return True
        return False