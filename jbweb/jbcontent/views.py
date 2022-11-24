from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Episode, Show
from .forms import SearchForm

import ipdb

class Landing(View):
    """
    """
    template = 'index.html'
    def get(self, request):
        """
        """
        search_form = SearchForm()
        shows = Show.objects.all()
        return render(
            request,
            self.template,
            {
                'shows': shows,
                'search_form': search_form
            },
        )
    def post(self, request):
        """
        """
        search_form = SearchForm(request.POST)
        
        if search_form.is_valid():
            #ipdb.set_trace()
            forward_url = '/search/?q=' + search_form.cleaned_data['q'] + '&models=jbcontent.episode'
            return redirect(forward_url)


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