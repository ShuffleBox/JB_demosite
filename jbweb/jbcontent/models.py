from django.db import models



class Show(models.Model):
    """
    show catchall
    """
    show_name = models.SlugField(unique=True)
    fancy_name = models.CharField(max_length=200, default='verbose name of a show')
    fancy_description = models.CharField(max_length=250, default='A description of a JB Show!')

    def __unicode__(self):
        return str(self.show_name)

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
    vtt_link = models.FileField(upload_to='media/vtt/')
    transcript_link = models.FileField(upload_to='media/vtt/')
    transcript = models.TextField()
    
    # we will want to check that the vtt exists so we can use that 
    # to render our template correctly. This check is new to me
    # so it will probably be dopey and broken at first.
    def _vtt_exists(self): 
        return self.vtt_link.storage.exists(self.vtt_link.name)
    vtt_exists = property(_vtt_exists)

    def _transcript_exists(self):
        return self.transcript_link.storage.exists(self.transcript_link.name)
    transcript_exists = property(_transcript_exists)

    def __unicode__(self):
        return str(self.ep_title)