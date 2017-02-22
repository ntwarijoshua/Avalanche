from rest_framework.permissions import BasePermission


class IsNotAnonymous(BasePermission):
	def has_permission(self,request,view):
		if request.user is None:
			return False
		else:
			return True

