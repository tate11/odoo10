 @api.multi
def record_loans(self):
	for wizard in self:
		books = wizard .book_ids
		loan = self.env['library.book.loan']
		for book in wizard.book_ids:
			values = self._prepare_loan(book)
			loan.create(values)
@api.multi
def _prepare_loan(self, book):
	return {'member_id': self.member_id.id,
		'book_id': book.id}
