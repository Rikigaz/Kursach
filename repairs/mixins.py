from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin

from repairs.models import Status
from users.models import Role

User = get_user_model()


class CustomerLoginRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if (
            request.user.is_authenticated and
            request.user.role == Role.CUSTOMER
        ):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class RepairMixin:

    @staticmethod
    def _get_repair_filter(user: User) -> dict:
        repair_filter = {
            Role.CUSTOMER: {
                'users': user
            },
            Role.TECHNICIAN: {
                'status__in': [
                    Status.CREATED,
                    Status.VERIFICATION,
                ]
            },
            Role.MASTER: {
                'status__in': [
                    Status.CONFIRMED,
                    Status.TESTS,
                ]
            },
            Role.WORKER: {
                'status__in': [
                    Status.RE_REPAIR,
                    Status.READY_TO_WORK,
                    Status.PROGRESS,
                ]
            }
        }
        return repair_filter.get(user.role)
