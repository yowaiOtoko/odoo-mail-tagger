from odoo import models
import logging

_logger = logging.getLogger(__name__)

class MailMail(models.Model):
    _inherit = 'mail.mail'

    def _send(self, auto_commit=False, raise_exception=False, smtp_session=None):
        """Add Brevo tag before sending any email"""
        for mail in self:
            # Build a meaningful tag. You can customize this logic.
            db_name = self.env.cr.dbname
            company_name = self.env.company.name.replace(" ", "_").lower() if self.env.company else ""

            tag = f"tenant:{db_name}"
            if company_name:
                tag += f",client:{company_name}"

            # Add the header (Brevo accepts one or multiple tags separated by comma)
            if not mail.headers:
                mail.headers = {}

            # Option 1: Simple single tag
            mail.headers['X-Mailin-Tag'] = tag

            # Option 2: Multiple tags (recommended)
            # mail.headers['X-Mailin-Tag'] = f"{tag},saas,transactional"

        return super()._send(auto_commit=auto_commit, raise_exception=raise_exception, smtp_session=smtp_session)