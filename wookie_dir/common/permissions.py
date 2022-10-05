from rest_framework.permissions import BasePermission

class BookViewPermission(BasePermission):

    def is_blacklisted_user(self, request):
        user = request.user
        return user.username in ['darth-vader']
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        # blacklisted users cannot perform post action
        if request.method == 'POST' and self.is_blacklisted_user(request):
            return False

        return bool(request.user and request.user.is_authenticated)
