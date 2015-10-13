from ..models import Harvest


def create_test_harvest(user, field, crop, unit, amount=4.2, hours=1.5, **kwargs):
    """
    Create and return a test Harvest object
    """
    create_kwargs = {
        'user': user,
      	'field': field,
      	'crop': crop,
      	'unit': unit,
      	'amount': amount,
      	'hours': hours,
    }
    create_kwargs.update(kwargs)
    return Harvest.objects.create(**create_kwargs)
