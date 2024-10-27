from furryFunnies.utils import get_user_obj


class ProfileObjectMixin:
    def get_object(self, queryset=None):
        return get_user_obj()
