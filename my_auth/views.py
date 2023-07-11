from django.shortcuts import render

# Create your views here.
from django.db.models import BooleanField, Case, Value, When
from django.shortcuts import get_object_or_404
from django.utils import timezone


from datetime import timedelta



from django.contrib.auth.models import User
from online_users.models import OnlineUserActivity

def homeview(request,user_id):
    min_time = timezone.now() - timedelta(hours=87600)
    queryset = OnlineUserActivity.objects.filter(user_id=user_id).annotate(
    is_online=Case(
        When(last_activity__gte=timezone.now() - timedelta(minutes=15), then=Value(True)),
        default=Value(False),
        output_field=BooleanField(),
    ))
    online_user_activity = get_object_or_404(queryset)
    context = {'online_user_activity': online_user_activity}
    return render(request, 'index.html', context)


