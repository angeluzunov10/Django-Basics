from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def sum_prices(queryset):
    return queryset.aggregate(Sum('price'))['price__sum'] or 0