# -*- coding: utf-8 -*-
{
    'name': "Gestor Videjuegos",

    'summary': """Muestra una lista de videojuegos""",

    'description': """Muestra una lista de videojuegos, con informacion del mismo y reservas.""",

    'author': "Manuel Ángel Mazás De Jesús",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': 'Beta 0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/games.xml',
        'views/games_categ.xml',
        'views/games_reserve.xml',
        'views/games_client.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
