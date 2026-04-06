# Odoo Mail Tagger

This Odoo module automatically adds Brevo tags to outgoing emails based on the tenant (database name) and client (company name).

## Features

- Automatically tags all outgoing emails with Brevo-compatible headers
- Uses database name as tenant identifier
- Includes company name as client identifier when available
- Compatible with Brevo's X-Mailin-Tag header format

## Installation

1. Place this module in your Odoo addons directory
2. Update your module list in Odoo
3. Install the "Mail Tagger" module

## Configuration

No additional configuration is required. The module automatically activates when installed.

## Tag Format

The module generates tags in the following format:
- `tenant:{database_name}`
- `client:{company_name}` (if company name is available)

Example: `tenant:production_db,client:my_company`

## Technical Details

The module inherits from `mail.mail` and overrides the `_send` method to add the `X-Mailin-Tag` header before sending emails.

## Compatibility

- Odoo 15.0+
- Requires the `mail` module
- Compatible with Brevo SMTP service