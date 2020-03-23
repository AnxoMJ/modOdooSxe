# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BookCategory(models.Model):
    _name = 'games.category'

    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Género')
    description = fields.Text('Descripción')
    parent_id = fields.Many2one(
        'games.category',
        string='Categoria Padre',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'games.category', 'parent_id',
        string = 'Categorias Hijas')
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('No puedes crear categorias recursivas!!!')
