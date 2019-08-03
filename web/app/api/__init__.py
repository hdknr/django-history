from django.contrib.sites.shortcuts import get_current_site


def get_absolute_path(request, path):
    if request:
        return request.build_absolute_uri(path)
    site = get_current_site(request)
    return f"http://{site.domain}/{path}" 