from django.utils import timezone

from apps.user.models import User


class LastActivity:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


    def process_view(self, request, view_func, view_args, view_kwargs):
        for user in User.objects.all():
            if user.hide_status==False:
                if user.last_action==None:
                    user.last_action=timezone.now()
                if (timezone.now() - user.last_action) < timezone.timedelta(minutes=2):
                    pass
                else:
                    user.is_online=False
                    user.save()
            elif user.hide_status==True:
                user.is_online=None
                user.last_action=None
                user.save()
                
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            if user.hide_status==False:
                user.last_action = timezone.now()
                user.is_online=True
                user.save()

                
