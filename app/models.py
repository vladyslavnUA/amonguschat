from django.db import models 
    
#parent model
class forum(models.Model):
    game_name=models.CharField(max_length=200, null=True)
    code=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.game_name)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)