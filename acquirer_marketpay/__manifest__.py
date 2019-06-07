# Copyright 2019 ingenieriacloud

{
    'name': 'acquirer marketpay',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer: marketpay Implementation',
    'version': '1.0',
    'author': "Pedro Baños,"
              ,
    'depends': [
        'payment',
        'website_sale',
    ],

    'data': [
        'views/marketpay.xml',
        'views/payment_acquirer.xml',
        'views/payment_marketpay_templates.xml',
        'data/payment_marketpay.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
}
