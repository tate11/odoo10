@api.model
def get_email_addresses(self, partner):
    partner.ensure_one()
    return partner.mapped('child_ids.email')

@api.model
def get_companies(self, partners):
    return partners.mapped('parent_id')
