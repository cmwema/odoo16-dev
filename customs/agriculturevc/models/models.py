# -*- coding: utf-8 -*-
from odoo import fields, models


class Actor(models.Model):
    _name = 'agriculturevc.actor'
    _description = ""
    _table = 'agriculturevc_actor'

    name = fields.Char(string='Name', required=True)
    venue = fields.Char(string='Venue', required=True)
    role = fields.Selection([
        ('maker', 'Maker'),
        ('processor', 'Processor'),
        ('trader', 'Trader'),
        ('mover', 'Mover'),
        ('consumer', 'Consumer'),
    ], string='Role', default='maker', required=True)


class Input(models.Model):
    _name = 'agriculturevc.input'
    _description = ""
    _table = 'agriculturevc_input'

    name = fields.Char(string='Name', required=True)
    is_available = fields.Boolean(string='Is Available', required=True)
    value = fields.Selection([
        ('financial', 'Financial'),
        ('social', 'Social'),
        ('natural', 'Natural'),
    ], string='value', default='financial', required=True)
    category = fields.Selection([
        ('knowledge', 'Knowledge'),
        ('labor', 'Labor'),
        ('resources', 'Resources'),
        ('tools', 'Tools'),
    ], string='Category', required=True)

    # Conditional fields
    # resources
    resource_type = fields.Selection([
        ('natural', 'Natural'),
        ('processed', 'Processed'),
    ], string='Role')

    # labor
    labor_level = fields.Selection([
        ('', ''),
    ], string='Labor level')
    labor_type = fields.Selection([], string='Labor type')

    # Knowledge
    knowledge_type = fields.Selection([
        ('experiential', 'Experiential'),
        ('validated', 'Validated'),
        ('unvalidated', 'Unvalidated'),

    ], string='Knowledge type', default='experiential')

    # tool
    tool_type = fields.Selection([
        ('manual', 'Manual'),
        ('mechanized', 'Mechanized'),
        ('digital', 'Digital'),
    ], string='Knowledge type', default='experiential')


class Asset(models.Model):
    _name = 'agriculturevc.asset'
    _description = ""

    name = fields.Char(string='Name')
    is_tangible = fields.Boolean(string='Is Tangible')
    volume_measure = fields.Float(string='Volume measure')
    volume_variant = fields.Float(string='Volume variant')
    quality_measure = fields.Float(string='Quality measure')
    quality_variant = fields.Float(string='Quality variant')
    input_value = fields.Float(string='Input Value')
    trade_value = fields.Float(string='Trade Value')
    stage = fields.Selection([
        ('production', 'Production'),
        ('processed', 'Processed'),
        ('byproduct', 'By Product'),
    ], string='stage', track_visibility='onchange')


class Action(models.Model):
    _name = 'agriculturevc.action'
    _description = ""
