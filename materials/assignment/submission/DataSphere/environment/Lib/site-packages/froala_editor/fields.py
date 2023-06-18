from django.db.models import Field
from django.forms import Textarea

from froala_editor.widgets import FroalaEditor
from django.conf import settings

from . import PLUGINS, THIRD_PARTY


class FroalaField(Field):
    description = "Froala Editable Field"

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        self.theme = kwargs.pop('theme', getattr(settings, 'FROALA_EDITOR_THEME', None))
        self.plugins = kwargs.pop('plugins', getattr(settings, 'FROALA_EDITOR_PLUGINS', PLUGINS))
        self.third_party = kwargs.pop('plugins', getattr(settings, 'FROALA_EDITOR_THIRD_PARTY', THIRD_PARTY))
        self.image_upload = kwargs.pop('image_upload', True)
        self.file_upload = kwargs.pop('file_upload', True)
        self.use_froala = kwargs.pop('', getattr(settings, 'USE_FROALA_EDITOR', True))
        super(FroalaField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        if self.use_froala:
            widget = FroalaEditor(options=self.options, theme=self.theme, plugins=self.plugins,
                                  image_upload=self.image_upload,
                                  file_upload=self.file_upload, third_party=self.third_party)
        else:
            widget = Textarea()
        defaults = {'widget': widget}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^froala_editor\.fields\.FroalaField"])
except ImportError:
    pass
