from django.views.generic import DetailView

from excuses.core.models import Excuse


class Home(DetailView):
    def get_object(self, queryset=None):
        return Excuse.objects.order_by('?')[0]

