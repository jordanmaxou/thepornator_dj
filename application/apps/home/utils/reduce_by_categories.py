def reduce_by_categories(acc, value):
    if value.category.slug not in acc.keys():
        acc[value.category.slug] = {
            "slug": value.category.slug,
            "name": value.category.name,
            "description": value.category.description,
            "icon": value.category.icon,
            "position": value.category.position,
            "websites": [],
        }
    acc[value.category.slug]["websites"].append(
        {
            "slug": value.slug,
            "name": value.name,
            "icon": value.icon,
            "is_direct_link": value.is_direct_link,
            "url": value.url,
            "note": value.avg_note_update,
            "has_running_deal": value.has_running_deal,
        }
    )
    return acc
