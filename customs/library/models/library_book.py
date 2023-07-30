from odoo import fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    _order = "name, date_published desc"
    _recname = "name"
    _table = "library_book"
    _log_access = True
    _auto = True
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner",
                                   string="Publisher")
    author_ids = fields.Many2many("res.partner",
                                  string="Authors")

    def check_isbn(self):
        self.ensure_one()

        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderators = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12],
                                           ponderators)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        if not self.isbn:
            raise ValidationError(f"Please provide an ISBN for {self.name}")
        if self.isbn and not self.check_isbn():
            raise ValidationError(f"{self.isbn} ISBN is invalid")

        return True
