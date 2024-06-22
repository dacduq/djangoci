from django.db import models
from django.utils.translation import gettext as _


class Blog(models.Model):
    title = models.CharField(_("titulo"), max_length=128)
    subtitle = models.CharField(_("subtitulo"), max_length=64)
    content = models.CharField(_("contenido"), max_length=1280)
    