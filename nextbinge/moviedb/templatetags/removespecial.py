from django import template

register = template.Library()

@register.filter
def removespecial(value):
    return value.replace(":","").replace("'","").replace(" ","_").replace(".", "").replace("&", "")