# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api, _

class invoice(models.Model):
    _inherit = 'account.invoice'

    def clean_internal_number(self):
        self.move_name = False
