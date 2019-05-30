from tastypie.resources import ModelResource
from User.models import User
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        authorization = Authorization()
