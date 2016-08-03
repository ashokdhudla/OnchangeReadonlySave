# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of web_readonly_save,
#     an Odoo module.
#
#     Copyright (c) 2015 AshokDhudla
#
#     web_readonly_save is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     web_readonly_save is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with web_readonly_save.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Onchange Read Only Save',
    'version': '1.0',
    "author": "AshokDhudla",
    "maintainer": "AshokDhudla",
    "website": "https://www.linkedin.com/in/ashok-dhudla-96a11358",
    'category': 'Technical Settings',
    'depends': [
        'web',
    ],
    'summary': 'Allow to save onchange modifications to readonly fields',
    'data': [
        'views/readonly_save.xml',
    ],
    'installable': True,
    'auto_install': False,
}
