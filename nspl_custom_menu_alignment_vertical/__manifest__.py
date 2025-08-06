# -*- coding: utf-8 -*-
{
    'name': 'Vertical Custom Menu',
    'version': '18.0',
    'summary': 'Custom vertical and categorized menu enhancements.',
    'description': """
This module combines functionalities from multiple RCL menu customization modules:

✔ Enables vertical menu view  
✔ Adds support for menu categories  
✔ Provides backend settings for toggling features
    """,
    'category': 'Tools',
    'sequence': 10,
    'author': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'company': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com',
    'support': 'support@namahsoftech.com',
    'price': 49.99,
    'currency': 'USD',
    'contributors': ['Jainil Joshi'],
    'license': 'LGPL-3',
    'depends': ['web_enterprise'],
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'nspl_custom_menu_alignment_vertical/static/src/js/home_menu_patch.js',
            'nspl_custom_menu_alignment_vertical/static/src/xml/home_menu.xml',
        ],
    },
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
