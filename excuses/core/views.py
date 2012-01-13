from django.views.generic import DetailView

from excuses.core.models import Excuse


class Home(DetailView):
    def getobject(self, queryset=None):
        return Excuse()

