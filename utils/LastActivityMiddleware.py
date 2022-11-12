from django.utils import timezone

from apps.user.models import User


class LastActivity:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        c= self.get_response(request)


        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.last_action = timezone.now()
            user.save()
        return c