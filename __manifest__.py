# -*- coding: utf-8 -*-
{
    'name': 'Mail Tagger',
    'version': '19.0.1.0.0',
    'author': 'Invo Facturation',
    'website': 'https://invo-facturation.fr',
    'license': 'LGPL-3',
    'category': 'Mail',
    'summary': 'Automatically add Brevo tags to outgoing emails',
    'description': """
Mail Tagger
===========

This module automatically adds Brevo tags to outgoing emails based on the tenant (database name) and client (company name).

Tags format:
- tenant:{database_name}
- client:{company_name} (if available)

The tags are added as X-Mailin-Tag headers that Brevo recognizes for email categorization and analytics.
    """,
    'depends': ['mail'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}