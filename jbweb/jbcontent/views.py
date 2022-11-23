from django.shortcuts import render
from django.views.generic import View

from .models import Episode, Show
import ipdb

class Landing(View):
    """
    """
    template = 'index.html'
    def get(self, request):
        """
        """
        shows = Show.objects.all()
        return render(
            request,
            self.template,
            {
                'shows': shows,
            },
        )

class ShowContents(View):
    """
    """
    template = 'show_list.html'
    def get(self, request, show_title):
        """
        """
        show = Show.objects.get(show_name=show_title)
        episode_set = show.episode_set.all()
        #this has to be an expensive way to filter for file presence
        #we should probably just put it in the DB
        episode_list = []
        for episode in episode_set:
            if episode.vtt_exists:
                episode_list.append(episode)
        
        return render(
            request,
            self.template,
            {
                'episodes': episode_list,
                'show': show,
            },
        )

class EpisodePlayback(View):
    """
    """
    template = 'play.html'
    def get(self, request, show_title, episode_number):
        """
        """
        
        jbshow = Show.objects.get(show_name=show_title)
        episode = Episode.objects.get(episode=episode_number, show=jbshow)
        
        return render(
            request,
            self.template,
            {
                'episode': episode,
                'show': jbshow,
            },
        )