from rest_framework import permissions

class IsOwnerOrAdminReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS like GET, HEAD, OPTIONS are allowed for any request
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            # If the user is admin or the owner, allow write access
            return obj.owner == request.user or request.user.is_staff
            
        except Exception as e:
        # Log the exception or print it for debugging
            print(f"Error in permission check: {e}")
            return False

class IsSupporterOrAdminReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.supporter == request.user or request.user.is_staff
        
        except Exception as e:
        # Log the exception or print it for debugging
            print(f"Error in permission check: {e}")
            return False    
        
        
class IsSelfOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj== request.user or request.user.is_superuser
        
        except Exception as e:
        # Log the exception or print it for debugging
            print(f"Error in permission check: {e}")
            return False    