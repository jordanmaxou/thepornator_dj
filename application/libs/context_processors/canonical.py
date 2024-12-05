def canonical(request):
    return {"canonical": request.build_absolute_uri(request.path)}
