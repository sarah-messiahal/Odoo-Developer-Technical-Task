# {
#     'name': 'Broker Management',
#     'version': '1.0',
#     'category': 'Real Estate',
#     'summary': 'Manage brokers, properties, and commissions.',
#     'description': """
#         This module allows you to manage brokers, assign them to properties, and calculate commissions.
#         It includes features such as creating brokers, tracking properties they handle, and generating commission reports.
#     """,
#     'author': 'Confident Real Estate',
#     'website': 'https://confident-group.ae',
#     'depends': ['base', 'sale', 'account'], 
#     'data': [
#         'security/ir.model.access.csv',
#         'views/broker_view.xml',
#         'views/sale_order_view.xml', 
#     ],
#     'installable': True,
#     'application': True,
#     'auto_install': False,
# }
{
    'name': 'Broker Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage brokers and link them to sale orders',
    'author': 'Your Name',
    'depends': ['sale'],  
    'data': [
        'security/ir.model.access.csv',  
        'views/broker_view.xml',         
        'views/sale_order_view.xml',     
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}