from django import template

register = template.Library()

@register.filter(name="update_param")
def update_page_number(value):
    li = value.split("page=")
    d = li[0]+'page='+'1'
    return d

@register.simple_tag
def setvar(val=None):
  return val