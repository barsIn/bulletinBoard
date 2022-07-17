from django import template

from board.models import Advertisement, Response, User

register = template.Library()


@register.simple_tag()
def get_my_responses(adv):
    if  Response.objects.filter(advertisement=adv).exists():
        return len(Response.objects.filter(advertisement=adv))
    else:
        return 0


@register.simple_tag()
def get_my_responses_list(adv):
    if  Response.objects.filter(advertisement=adv).exists():
        return Response.objects.filter(advertisement=adv)
    else:
        return None


@register.simple_tag()
def get_userpost_list(user):
    if  Advertisement.objects.filter(author=user).exists():
        posts = Advertisement.objects.filter(author=user)
        return posts
    else:
        return None

@register.simple_tag()
def get_resp_list(post):
    if Response.objects.filter(advertisement=post).exists():
        return Response.objects.filter(advertisement=post)
    else:
        return None
