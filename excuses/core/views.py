from random import choice

from django.views.generic import DetailView

from excuses.core.models import Excuse


class Home(DetailView):
    def get_object(self, queryset=None):
        excuses = Excuse.objects.all()
        excuse_pks = [pk[0] for pk in excuses.values_list('pk')]
        return excuses.get(pk=choice(excuse_pks))

