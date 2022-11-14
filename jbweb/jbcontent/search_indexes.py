import datetime
from haystack import indexes
from jbcontent.models import Episode


class EpisodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    summary = indexes.CharField(model_attr='summary')
    title = indexes.CharField(model_attr='ep_title')
    show = indexes.CharField(model_attr='show')

    def get_model(self):
        return Episode

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
