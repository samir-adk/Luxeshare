import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            logger.debug(f"User {username} found in the database.")
        except UserModel.DoesNotExist:
            logger.debug(f"User {username} not found in the database.")
            return None
        else:
            if user.check_password(password):
                logger.debug(f"Password for user {username} is correct.")
                return user
            else:
                logger.debug(f"Password for user {username} is incorrect.")
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
