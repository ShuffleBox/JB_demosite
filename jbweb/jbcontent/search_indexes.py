import datetime
from haystack import indexes 
from jbcontent.models import Episode

import ipdb

class EpisodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    summary = indexes.CharField(model_attr='summary')
    title = indexes.CharField(model_attr='ep_title')
    show = indexes.CharField(model_attr='show')
    transcript = indexes.CharField(model_attr='transcript')

    def get_model(self):
        #ipdb.set_trace()
        return Episode

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    #def prepare_transcript(self, obj):
    #    return self.transcript_link.readlines()
'''
    def prepare(self, obj):
        data = super(EpisodeIndex, self).prepare(obj)
        #file_data = self._get_backend(None).extract_file_contents(obj.transcript_link)
        template = loader.select_template(
            ("search/indexes/jbcontent/episode_text.txt", ),
        )
        data["text"] = template.render(Context({
            "object": obj,
        }))
        return data
'''