import datetime
from django.utils import timezone

def time_since_posted(post_time):
    now = timezone.now()
    diff = now - post_time

    if diff.days == 0:
        if diff.seconds < 60:
            return "à l'instant"
        elif diff.seconds < 3600:
            return f"il y a {diff.seconds // 60} minutes"
        elif diff.seconds < 86400:
            return f"il y a {diff.seconds // 3600} heures"
    elif diff.days < 7:
        return f"il y a {diff.days} jours"
    else:
        return post_time.strftime("%d %b, %Y")  # Exemple: "12 janv., 2024"
