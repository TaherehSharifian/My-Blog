from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post-images', null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()


    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    comment = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.username} - {self.post.title}'