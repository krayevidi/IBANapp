from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from bank_accounts.searializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.user.account_set.all()

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
