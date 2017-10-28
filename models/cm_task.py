# -*- conding: utf-8 -*-

from odoo import models, fields, api

class CustomerTask(models.Model):
    _name = 'cm.task'
    _description = 'Customer Task'

    name = fields.Char('Description', required=True)
    customer_id = fields.Many2one('res.partner', 'Customer')
    req_time = fields.Datetime('Time Required')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    color = fields.Integer()

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True
    
    @api.multi
    def do_clear_done(self):
        done = self.search([('is_done', '=', True)])
        done.write({'active': False})
        return True
