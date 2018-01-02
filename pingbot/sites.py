_indexed_site_aliases = {
    "admins": ["admin"]
}

_site_aliases = {alias: id for (id, aliases) in _indexed_site_aliases.items() for alias in aliases}

def canonical_site_id(site_id):
    return _site_aliases.get(site_id, site_id)

_site_names = {
    'mathoverflow': 'mathoverflow.net'
}

def site_name(site_id):
    return _site_names.get(site_id, '{}.stackexchange.com'.format(site_id))
