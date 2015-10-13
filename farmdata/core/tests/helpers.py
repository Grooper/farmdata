from PIL import Image

from ..utils import get_pil_image_as_django_content_file
from ..models import User, Farm, Crop, Unit, UnitConversion, Field


def create_test_image(filename='test.png', size=(160, 160), color='green'):
    """
    Create and return a test image as a ContentFile
    """
    image = Image.new('RGBA', size, color)
    image_content_file = get_pil_image_as_django_content_file(image, 'png')
    image_content_file.name = filename
    return image_content_file


def create_test_user(email='test@example.com', password='test', first_name='Test', last_name='User', **kwargs):
    """
    Create and return a test User object
    """
    create_kwargs = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
    }
    create_kwargs.update(kwargs)
    return User.objects.create_user(**create_kwargs)


def create_test_farm(owner, name='Dickinson College Farm', **kwargs):
    """
    Create and return a test Farm object
    """
    create_kwargs = {
        'owner': owner,
        'name': name,
    }
    create_kwargs.update(kwargs)
    return Farm.objects.create(**create_kwargs)


def create_test_crop(default_unit, name='Test Crop', **kwargs):
    """
    Create and return a test Crop object
    """
    create_kwargs = {
        'name': name,
        'default_unit': default_unit,
    }
    create_kwargs.update(kwargs)
    return Crop.objects.create(**create_kwargs)


def create_test_unit(name='Test Unit', **kwargs):
    """
    Create and return a test Unit object
    """
    create_kwargs = {
        'name': name,
    }
    create_kwargs.update(kwargs)
    return Unit.objects.create(**create_kwargs)


def create_test_unit_conversion(crop, unit, conversion=1.5, **kwargs):
    """
    Create and return a test UnitConversion object
    """
    create_kwargs = {
        'crop': crop,
        'unit': unit,
        'conversion': conversion,
    }
    create_kwargs.update(kwargs)
    return UnitConversion.objects.create(**create_kwargs)


def create_test_field(name='Test Field', size='4.2', **kwargs):
    """
    Create and return a test Field object
    """
    create_kwargs = {
        'name': name,
        'size': size,
    }
    create_kwargs.update(kwargs)
    return Field.objects.create(**create_kwargs)
