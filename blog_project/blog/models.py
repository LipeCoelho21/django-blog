from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.caption
    
class Post(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    excerpt = models.CharField(max_length=200, null=False, blank=False)
    image_name = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now=True, auto_now_add=False, null=False, blank=False)
    slug = models.SlugField(unique=True, db_index=True, null=False, blank=False)
    content = models.TextField(validators=[MinLengthValidator(20)], null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=False, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

