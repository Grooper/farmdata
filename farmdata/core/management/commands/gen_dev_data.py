import os
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import User, Farm, Crop, Field
from ...tests.helpers import (create_test_user, create_test_farm, create_test_crop, create_test_unit,
                              create_test_unit_conversion, create_test_field)

from farmdata.harvest.models import Harvest
from farmdata.harvest.tests.helpers import create_test_harvest


class Command(BaseCommand):
    """
    gen_dev_data command
    Generate data for our local development environments.
    """
    def handle(self, *args, **kwargs):
        """
        Run gen_dev_data command
        """
        # Only run this command in development environment
        if not settings.DEBUG:
            print 'Only run this in development environment'
            return

        # Delete previous files in `/media/`
        print 'Deleting existing media files'
        folder = settings.MEDIA_ROOT
        if os.path.isdir(folder):
            shutil.rmtree(folder)

        #################### 1. USERS ####################
        print 'Creating Users'

        user_maurice = create_test_user(
            email='maurice@dickinson.edu',
            password='test',
            first_name='Maurice',
            last_name='Royce',
        )

        user_tim = create_test_user(
            email='tim@dickinson.edu',
            password='test',
            first_name='Tim',
            last_name='Kang',
        )

        user_matt = create_test_user(
            email='matt@dickinson.edu',
            password='test',
            first_name='Matt',
            last_name='Steiman',
        )

        user_john = create_test_user(
            email='johng307@gmail.com',
            password='test',
            first_name='John',
            last_name='G',
        )

        user_alpha = create_test_user(
            email='alpha@example.com',
            password='test',
            first_name='Alpha',
            last_name='Smith',
        )

        user_bravo = create_test_user(
            email='bravo@example.com',
            password='test',
            first_name='Bravo',
            last_name='Smith',
        )

        #################### 2. FARMS ####################
        print 'Creating Farms'

        farm_matt = create_test_farm(
            owner=user_matt,
            name='Dickinson College Farm',
            location='Carlisle, PA',
        )
        farm_matt.add_member(user_maurice)
        farm_matt.add_member(user_tim)

        farm_tim = create_test_farm(
            owner=user_tim,
            name='Tim\'s Farm',
            location='Santa Clara, CA'
        )
        farm_tim.add_member(user_maurice)
        farm_tim.add_member(user_alpha)
        farm_tim.add_member(user_bravo)

        farm_alpha = create_test_farm(
            owner=user_alpha,
            name='Alpha\'s Farm',
            location='California',
        )
        farm_alpha.add_member(user_bravo)
        farm_alpha.add_member(user_maurice)

        #################### 3. CROPS ####################
        print 'Creating Crops'

        # Create Units
        unit_pound = create_test_unit(
            name='Pound',
        )
        unit_bunch = create_test_unit(
            name='Bunch',
        )
        unit_ear = create_test_unit(
            name='Ear',
        )
        unit_liter = create_test_unit(
            name='Liter',
        )
        unit_quart = create_test_unit(
            name='Quart',
        )
        unit_pint = create_test_unit(
            name='Pint',
        )
        unit_each = create_test_unit(
            name='Each',
        )
        unit_head = create_test_unit(
            name='Head',
        )

        # Create Crops
        crop_bean = create_test_crop(
            name='Bean',
            default_unit=unit_pound,
        )

        crop_beet = create_test_crop(
            name='Beet',
            default_unit=unit_bunch,
        )
        create_test_unit_conversion(
            crop=crop_beet,
            unit=unit_pound,
            conversion=2.1,
        )
        create_test_unit_conversion(
            crop=crop_beet,
            unit=unit_quart,
            conversion=0.25,
        )

        crop_carrot = create_test_crop(
            name='Carrot',
            default_unit=unit_bunch,
        )
        create_test_unit_conversion(
            crop=crop_carrot,
            unit=unit_quart,
            conversion=1.7,
        )

        crop_leek = create_test_crop(
            name='Leek',
            default_unit=unit_bunch,
        )
        create_test_unit_conversion(
            crop=crop_leek,
            unit=unit_each,
            conversion=3.0,
        )

        create_test_crop(
            name='Lettuce',
            default_unit=unit_head,
        )

        crop_strawberry = create_test_crop(
            name='Strawberry',
            default_unit=unit_quart,
        )
        create_test_unit_conversion(
            crop=crop_strawberry,
            unit=unit_pint,
            conversion=2.0,
        )

        crop_watermelon = create_test_crop(
            name='Watermelon',
            default_unit=unit_each,
        )

        #################### 4. FIELDS ####################
        print 'Creating Fields'

        field_a = create_test_field(
            name='A',
            size=1.0,
            number_of_beds=20.5,
            length=425,
        )
        field_a_space = create_test_field(
            name='A SPACE',
            size=0.56,
            number_of_beds=8,
            length=610,
        )
        field_b = create_test_field(
            name='B',
            size=0.41,
            number_of_beds=12,
            length=300,
        )
        field_c = create_test_field(
            name='C',
            size=1.26,
            number_of_beds=10,
            length=1100,
        )
        field_d = create_test_field(
            name='D',
            size=0.52,
            number_of_beds=300,
            length=12,
        )
        field_x = create_test_field(
            name='X',
            size=0.43,
            number_of_beds=9,
            length=317,
        )
        field_y = create_test_field(
            name='Y',
            size=0.44,
            number_of_beds=10,
            length=295,
        )
        field_z = create_test_field(
            name='Z',
            size=0.38,
            number_of_beds=9,
            length=282,
        )

        #################### 5. HARVESTS ####################
        print 'Creating Harvests'

        create_test_harvest(
            user=user_maurice,
            field=field_a,
            crop=crop_bean,
            unit=unit_pound,
            amount=3,
            hours=0.25,
        )

        create_test_harvest(
            user=user_maurice,
            field=field_b,
            crop=crop_bean,
            unit=unit_pound,
            amount=11,
            hours=1.25,
        )

        create_test_harvest(
            user=user_tim,
            field=field_x,
            crop=crop_beet,
            unit=unit_bunch,
            amount=6,
            hours=1.67,
        )

        create_test_harvest(
            user=user_matt,
            field=field_a_space,
            crop=crop_strawberry,
            unit=unit_quart,
            amount=5,
            hours=0.33,
        )

        create_test_harvest(
            user=user_matt,
            field=field_b,
            crop=crop_strawberry,
            unit=unit_pint,
            amount=8,
            hours=.5,
        )

        #################### FINAL OUTPUT ####################
        print '-------------------- Users --------------------'
        print 'There are {} test users:'.format(User.objects.count())
        for user in User.objects.all():
            print ' * User {}:'.format(user.id)
            print '     - email: {}'.format(user.email)
            print '     - name: {}'.format(user.get_short_name())

        print '-------------------- Farms --------------------'
        print 'There are {} test farms:'.format(Farm.objects.count())
        for farm in Farm.objects.all():
            print ' * Farm {}:'.format(farm.id)
            print '     - name: {}'.format(farm.name)
            print '     - owner: {}'.format(farm.owner)

        print '-------------------- Crops --------------------'
        print 'There are {} test crops:'.format(Crop.objects.count())
        for crop in Crop.objects.all():
            print ' * Crop {}:'.format(crop.id)
            print '     - name: {}'.format(crop.name)
            print '     - default unit: {}'.format(crop.default_unit)

        print '-------------------- Fields --------------------'
        print 'There are {} test fields:'.format(Field.objects.count())
        for field in Field.objects.all():
            print ' * Field {}:'.format(field.id)
            print '     - name: {}'.format(field.name)
            print '     - size: {}'.format(field.size)

        print '-------------------- Harvests --------------------'
        print 'There are {} test harvests:'.format(Harvest.objects.count())
        for harvest in Harvest.objects.all():
            print ' * Harvest {}:'.format(harvest.id)
            print '     - user: {}'.format(harvest.user)
            print '     - crop: {}'.format(harvest.crop)
            print '     - field: {}'.format(harvest.field)
