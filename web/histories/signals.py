import django.dispatch


update_link_args = [
    "instance",
]

update_link = django.dispatch.Signal(providing_args=update_link_args)