from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.resources import ModelResource
from .models import Project

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class ProjectResource(ModelResource):
	created_by = fields.ForeignKey(UserResource, 'created_by')

	class Meta:
		queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()
        filtering = {"projet_name": ALL, "id":ALL, "created_by": ALL_WITH_RELATIONS}
