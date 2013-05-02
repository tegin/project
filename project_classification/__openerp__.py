# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
# All Right Reserved
#
# Author : Joel Grand-guillaume (Camptocamp)
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################


{
    'name': 'Project classification (easy hierarchy and setup for project managers)',
    'version': '1.0',
    'category': 'Generic Modules/Projects & Services',
    'description': """

This Module allow you to setup different project classification to ease the data entry of
new project. The parent project will be set as readonly to forbid users to change it.
The parent is still available through the analytic account object. This is useful because
this way, project manager will setup correctly the analytical account just by choosing the
corresponing classification.

A project classification is composed by :

 * A name
 * An Analytic Account which represent the parent project to set
 * An optional Invoice factor
 * An optional Account Manager
 * An optional Pricelist
 * An optional Currency

Those values will be set on a project when selecting a classification.

""",
    'author': 'Camptocamp',
    'website': 'http://www.camptocamp.com',
    'depends': ['project', 'hr_timesheet_invoice', 'analytic'],
    'data': [
        'project_classification_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: