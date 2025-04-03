from api.models import User


def create_or_save(user_def, to_update=None):
    try:
        user = User.objects.get(google_id=user_def["google_id"])
        for key, value in user_def.items():
            if to_update is not None:
                if key in to_update:
                    setattr(user, key, value)
        user.save(update_fields=to_update)
    except User.DoesNotExist:
        user = User(**user_def)
        user.save()
    return user
