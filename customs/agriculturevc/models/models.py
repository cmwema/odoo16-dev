# -*- coding: utf-8 -*-
from odoo import fields, models


class Venue(models.Model):
    """
    Venues are the places where Activities are performed.
    """
    _name = 'agriculturevc.venue'
    _description = ""
    _table = "agriculturevc_venue"

    name = fields.Char(string='Name')
    # Relationships
    actor_ids = fields.Many2many('agriculturevc.actor', string='Actors')
    asset_ids = fields.Many2many('agriculturevc.asset', string='Assets')
    input_ids = fields.Many2many('agriculturevc.input', string='Inputs')
    action_ids = fields.Many2many('agriculturevc.action', string='Actions')
    creation_date = fields.Datetime(string='Creation Date', readonly=True, default=lambda self: fields.Datetime.now())


class Actor(models.Model):
    """
    Actors are people who add value to the asset with their knowledge,
    their use of their own available inputs and their management of their venues.
    """
    _name = 'agriculturevc.actor'
    _description = "Actors are people who add value to the asset with their knowledge, \
    their use of their own available inputs and their management of their venues."
    _table = 'agriculturevc_actor'

    name = fields.Char(string='Name', required=True)
    venue_ids = fields.Many2many('agriculturevc.venue', string='Venues')
    asset_ids = fields.Many2many('agriculturevc.asset', string='Assets')
    input_ids = fields.Many2many('agriculturevc.input', string='Inputs')
    action_ids = fields.Many2many('agriculturevc.action', string='Actions')
    role = fields.Selection([
        ('maker', 'Maker'),
        ('processor', 'Processor'),
        ('trader', 'Trader'),
        ('mover', 'Mover'),
        ('consumer', 'Consumer'),
    ], string='Role', default='maker', required=True)
    creation_date = fields.Datetime(string='Creation Date', readonly=True, default=lambda self: fields.Datetime.now())


class Input(models.Model):
    """
    The components required to make an asset.
    """
    _name = 'agriculturevc.input'
    _description = "The components required to make an asset."
    _table = 'agriculturevc_input'

    name = fields.Char(string='Name', required=True)
    is_available = fields.Boolean(string='Is Available', required=True)
    # Relationships
    asset_ids = fields.Many2many('agriculturevc.asset', string='Assets')
    venue_ids = fields.Many2many('agriculturevc.venue', string='Venues')
    actor_ids = fields.Many2many('agriculturevc.actor', string='Actors')
    action_ids = fields.Many2many('agriculturevc.action', string='Actions')

    creation_date = fields.Datetime(string='Creation Date', readonly=True, default=lambda self: fields.Datetime.now())
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
    skill_level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], string='Skill Level')
    labor_type = fields.Selection([
        ('skilled', 'Skilled'),
        ('unskilled', 'Unskilled'),
        ('semiskilled', 'Semi-Skilled'),
    ], string='Labor type')

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
    """
    (Good or Service)
    Assets are the primary focus of the work that happens in the value chain.
    A product of combining inputs – work, resources and knowledge to create something of value
    for the purpose of exchange.
    """
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

    creation_date = fields.Datetime(string='Creation Date', readonly=True, default=lambda self: fields.Datetime.now())
    stage = fields.Selection([
        ('production', 'Production'),
        ('processed', 'Processed'),
        ('byproduct', 'By Product'),
    ], string='stage', track_visibility='onchange')

    # Relationships
    input_ids = fields.Many2many('agriculturevc.input', string='Inputs')
    venue_ids = fields.Many2many('agriculturevc.venue', string='Venues')
    actor_ids = fields.Many2many('agriculturevc.actor', string='Actors')
    action_ids = fields.Many2many('agriculturevc.action', string='Actions')


class Action(models.Model):
    """
    the work required to combine inputs to progress the asset through the value chain.
    """
    _name = 'agriculturevc.action'
    _description = ""

    name = fields.Char(string='Name')

    # Relationships
    input_ids = fields.Many2many('agriculturevc.input', string='Inputs')
    venue_ids = fields.Many2many('agriculturevc.venue', string='Venues')
    actor_ids = fields.Many2many('agriculturevc.actor', string='Actors')
    asset_ids = fields.Many2many('agriculturevc.asset', string='Asset')

    creation_date = fields.Datetime(string='Creation Date', readonly=True, default=lambda self: fields.Datetime.now())
