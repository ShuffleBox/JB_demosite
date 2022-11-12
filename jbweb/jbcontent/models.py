from django.db import models



class Show(models.Model):
    """
    show catchall
    """
    show_name = models.SlugField(unique=True)  #get from payments.library.unt.edu
    fancy_name = models.CharField(max_length=200)
    fancy_description = models.CharField(max_length=250)

    def __unicode__(self):
        return str(self.account_name)

class Episode(models.Model):
    """
    Individual episodes
    """
    show = models.ForeignKey(Show, on_delete=models.PROTECT)
    episode = models.IntegerField()
    ep_title = models.CharField(max_length=250)
    summary = models.TextField()
    url_link = models.URLField()
    audio_link = models.URLField()
    vtt_link = models.FileField(upload_to='vtt/')

