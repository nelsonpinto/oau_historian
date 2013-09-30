
from hist.models import Controller
from hist.models import Connection
from hist.models import Tag
from hist.models import Snapshot
from hist.models import History
from hist.models import Trendconfig
from hist.models import Mensaje


from django.contrib import admin

admin.site.register(Controller)
admin.site.register(Connection)
admin.site.register(Tag)
admin.site.register(Snapshot)
admin.site.register(History)
admin.site.register(Trendconfig)
admin.site.register(Mensaje)
