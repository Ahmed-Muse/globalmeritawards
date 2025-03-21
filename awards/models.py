from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('voter', 'category')  # Ensure one vote per category per voter
    def __str__(self):
        return f"{self.user.username} voted for {self.company.name} in {self.category.name}"
    
