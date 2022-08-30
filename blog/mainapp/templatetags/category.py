from django import template
from mainapp.models import PostCategory

register = template.Library()

@register.inclusion_tag('tags/categories_list.html')
def list_category():
    return {"categories": PostCategory.objects.all()}