from django.db.models import Count, Sum
from pyexpat.errors import messages

from FisherPoint.competition.models import Competition
from FisherPoint.message.models import Message


def get_competition_points(profile):
    first_places = Competition.objects.filter(first_place=profile).count()
    second_places = Competition.objects.filter(second_place=profile).count()
    third_places = Competition.objects.filter(third_place=profile).count()
    competition_points = first_places * 3 + second_places * 2 + third_places * 1

    return competition_points


def get_posts_number(profile):
    posts_number = Message.objects.filter(user=profile).count()

    return posts_number


def get_fish_number(profile):
    messages = Message.objects.filter(user=profile).aggregate(likes_number=Count('likes'))

    return messages['likes_number']
