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
        episodes = show.episode_set.all()
        #ipdb.set_trace()
        return render(
            request,
            self.template,
            {
                'episodes': episodes,
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
        #ipdb.set_trace()
        jbshow = Show.objects.get(show_name=show_title)
        episode = Episode.objects.get(episode=episode_number, show=jbshow)
        ipdb.set_trace()
        return render(
            request,
            self.template,
            {
                'episode': episode,
                'show': jbshow,
            },
        )