from django.db import models

# The topic a user is learning about
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # Return a string representation of the model
    def __str__(self):
        return self.text


# Something specific learned about a topic
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    # Return a string representation of the model
    def __str__(self):
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."


