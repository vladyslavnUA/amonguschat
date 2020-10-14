from django.db import models 

class forum(models.Model):
    game_name=models.CharField(max_length=200, null=True)
    code=models.CharField(max_length=6,null=True, help_text="Game code should be 6 characters")
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.game_name)
 
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)