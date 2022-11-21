from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from jbcontent.models import Show, Episode
import feedparser
import ipdb

class Command(BaseCommand):
    help = 'Sync contents'

    def add_arguments(self, parser):
        parser.add_argument('feed_urls', nargs='+', type=str)

    def handle(self, *args, **options):
        all_episodes = Episode.objects.all()

        for rss_url in options['feed_urls']:
            rss = feedparser.parse(rss_url)
            if len(rss['entries']) > 0:
                for episode in rss['entries']:
                    export_fields = {}
                    export_fields['show'] = slugify(rss['feed']['title'])
                    export_fields['ep_title'] = episode['title']
                    export_fields['summary'] = episode['summary']
                    export_fields['published'] = episode['published']
                    export_fields['links'] = episode['links']
                    export_fields['episode'] = episode['link'].split('/')[-1]
                    for link in export_fields['links']:
                        if link['type'] == 'audio/mp3' or link['type'] == 'audio/mpeg':
                            export_fields['audio_link'] = link['href']
                        elif link['type'] == 'text/html':
                            export_fields['url_link'] = link['href']
                    try:
                        export_fields['vtt_file'] = export_fields['audio_link'].split('/')[-1] + '.vtt'
                        export_fields['transcript_file'] = export_fields['audio_link'].split('/')[-1] + '.txt'
                    except KeyError:
                        print('audio format link not found on entry! what do?!')
                        ipdb.set_trace()

                    jbshow, created = Show.objects.get_or_create(
                        show_name = export_fields['show'],
                    )
                    
                    episode, created = Episode.objects.get_or_create(
                        episode = export_fields['episode'],
                        show = jbshow,
                        defaults = {
                            'show': jbshow,
                            'ep_title': export_fields['ep_title'],
                            'summary': export_fields['summary'],
                            'url_link': export_fields['url_link'],
                            'audio_link': export_fields['audio_link'],
                            'vtt_link': export_fields['vtt_file'],
                            'transcript_link': export_fields['transcript_file']
                            #'' = export_fields[''],
                            #'' = export_fields[''],
                            
                        }
                    )
                    setattr(episode,'ep_title',export_fields['ep_title'])
                    setattr(episode,'summary',export_fields['summary'])
                    setattr(episode,'url_link',export_fields['url_link'])
                    setattr(episode,'audio_link',export_fields['audio_link'])
                    setattr(episode,'vtt_link',export_fields['vtt_file'])
                    setattr(episode,'transcript_link',export_fields['transcript_file'])
                    
                    episode.save()
                    try:
                        setattr(episode,'transcript',episode.transcript_link.open().read().decode('utf8'))
                        episode.save()
                    except:
                        continue
                    print(episode.ep_title + " - " + episode.transcript_link.url)
                    #ipdb.set_trace()
'''
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll '%s' does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll '%s'' % poll_id))
'''