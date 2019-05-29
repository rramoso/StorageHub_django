from tastypie.resources import ModelResource
from User.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
