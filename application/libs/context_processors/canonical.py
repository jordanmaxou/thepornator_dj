def canonical(request):
    base_url = request.build_absolute_uri(request.path)
    if page := request.GET.get("page"):
        base_url += f"?page={page}"
    return {"canonical": base_url}
