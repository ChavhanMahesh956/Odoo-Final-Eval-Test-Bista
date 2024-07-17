{

    'name': 'Student Info',
    'author': 'Mahesh Chavhan  ',
    'version': '1.0',
    'category': 'Uncategorized',
    'depends': ['base', 'sale', 'website', 'website_payment'],
    'data':[
        # Security Files
        'security/ir.model.access.csv',
        'security/groups.xml',

         # Data Files
        'data/website_menu.xml',
        
        # View Files
        'views/college_view.xml',
        'views/course_view.xml',
        'views/enrollment_view.xml',
        'views/enrollment_confirmation_template.xml',
        'views/enrollment_web_page.xml',
        'views/sale_order_line_views.xml',
        'views/stock_picking_inherit_view.xml',
        'views/account_move_inherit_view.xml',
        # 'views/report_templates.xml',
        'views/menu_view.xml',

       
    ],
    'application': True,
    'installable': True,
    'license':'LGPL-3',

}