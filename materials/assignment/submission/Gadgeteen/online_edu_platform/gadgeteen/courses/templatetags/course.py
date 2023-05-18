from django import template


register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None

@register.filter
def percentof(part,whole):
    try:
        return "%d%%" % (float(part) / whole * 100)
    except (ValueError, ZeroDivisionError):
        return ""
    
@register.filter
def barpercentof(part,whole):
    try:
        return "%d%%" % ((float(part) / whole * 100)+30)
    except (ValueError, ZeroDivisionError):
        return ""
