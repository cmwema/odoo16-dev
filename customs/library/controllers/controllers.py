# -*- coding: utf-8 -*-
from odoo import http


class Library(http.Controller):
    @http.route('/library/library', auth='public')
    def index(self, **kw):
        return "Hello, world"

    # @http.route("/library/books")
    # def list(self, **kwargs):
    #     book = http.request.env["library.book"]
    #     books = book.search([])
    #     return http.request.render(
    #         "library.book_list_template",
    #         {"book": books}
    #     )
