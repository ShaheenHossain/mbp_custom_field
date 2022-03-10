# -*- coding: utf-8 -*-

from odoo import fields, models, _, api


class PartNumberInherit(models.Model):
    _inherit = "product.template"

    part_no = fields.Char("Part Number")

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_ref = fields.Char("Customer Ref")
    representative = fields.Many2one('res.users', string='Rep')
    operator = fields.Many2one('res.users', string='Operator', default=lambda self: self.env.user, tracking=True)
    picked_by = fields.Many2one('res.users', string='Picked By', default=lambda self: self.env.user, tracking=True)

    account_no = fields.Char("Account No.")



class QuotationLineFrFieldInherit(models.Model):
    _inherit = "sale.order.line"

    part_no = fields.Char(related="product_id.part_no", string="Part Number")
    # goods_price = fields.Float(string="Goods")

    # @api.onchange("product_id")
    # def get_good_price(self):
    #     self.goods_price=self.price_unit





class MbppartAccount(models.Model):
    _inherit = 'account.move.line'

    part_no = fields.Char(related="product_id.part_no", string="Part Number")
