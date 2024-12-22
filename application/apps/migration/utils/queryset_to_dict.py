def queryset_to_dict(queryset, field):
    return {getattr(obj, field): obj for obj in queryset}
