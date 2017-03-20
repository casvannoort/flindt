from django.contrib import admin
from django.utils.translation import ugettext as _

from django_object_actions import DjangoObjectActions

from .models import Round
from .manager import RoundManager, NoSolutionPossible


class RoundAdmin(DjangoObjectActions, admin.ModelAdmin):
    def start_round(self, request, obj):
        round_manager = RoundManager(obj)
        try:
            round_manager.start_round()
            obj.message_for_open()
        except NoSolutionPossible:
            self.message_user(request, 'Not possible to start a round when users are included that do not fulfill any role!')

    start_round.label = _('Start the round')
    start_round.short_description = "This will create feedback objects."

    change_actions = ('start_round',)


admin.site.register(Round, RoundAdmin)