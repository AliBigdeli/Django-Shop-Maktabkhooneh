from django.contrib.auth.mixins import UserPassesTestMixin
from accounts.models import UserType


class HasCustomerAccessPermission(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.type == UserType.customer.value
        return False
    

class HasAdminAccessPermission(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.type == UserType.admin.value
        return False