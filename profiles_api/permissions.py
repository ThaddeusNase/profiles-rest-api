from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = HTTP methode die KEINE Veränderungen am Object machen -> z.B get
        # also wenn request.method = innerhalb von SAFE_METHODS-Liste ist, dann können User andere Profile SEHEN ABER NICHT VERÄNDERN!
        if request.method in permissions.SAFE_METHODS:
            return True

        # wenn request.method aber z.B put/patch/delete (außerhalb von permissions.SAFE_METHODS)
        # -> dann checken ob dem User auch das Profile gehört, damit nicht jeder user das profile von einem anderen manipulieren kann
        else:
            return obj.id == request.user.id



# allow users to update their own status
class UpdateOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # check the user is trying to update their own status
        if request.method in permissions.SAVE_METHODS:
            return True

        # wenn request keine SAVE_METHOD, dann checken ob der user auch authorisiert ist, den status zur ändern
        return obj.user_profile.id == request.user.id
