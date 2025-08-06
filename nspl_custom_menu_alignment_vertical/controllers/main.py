# -*- coding: utf-8 -*-
# This file is part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class HomeMenuCategoryController(http.Controller):

    @http.route('/web/custom_app_categories', type='json', auth='user', csrf=False)
    def get_app_categories(self):
        fixed_categories = [
            'sales', 'services', 'accounting', 'inventory', 'manufacturing', 'website', 'marketing',
            'human resources', 'productivity', 'customizations', 'repair', 'internet of things',
            'localization', 'purchases'
        ]

        def normalize(cat):
            return cat.strip().lower().replace('/', '').replace(' ', '') if cat else ''

        custom_titles = {
            'humanresources': 'HR',
            'accounting': 'Accounts',
            'internetofthings': 'IoT',
        }

        fixed_normalized = {
            normalize(cat): custom_titles.get(normalize(cat), cat.title())
            for cat in fixed_categories
        }

        modules = request.env['ir.module.module'].sudo().search([('state', '=', 'installed')])
        result = {}
        for mod in modules:
            cat_name = mod.category_id.name if mod.category_id else None
            parent_cat_name = mod.category_id.parent_id.name if mod.category_id and mod.category_id.parent_id else None

            norm = normalize(cat_name)
            parent_norm = normalize(parent_cat_name)

            if norm in fixed_normalized:
                result[mod.name] = fixed_normalized[norm]
            elif parent_norm in fixed_normalized:
                result[mod.name] = fixed_normalized[parent_norm]
            else:
                result[mod.name] = 'Others'

        return result


class MenuLayoutController(http.Controller):

    @http.route('/web/session/get_company_menu_layout_vertical', type='json', auth='user')
    def get_company_menu_layout_vertical(self):
        layout = request.env.user.company_id.menu_layout_vertical or 'default'
        return {'layout': layout}
