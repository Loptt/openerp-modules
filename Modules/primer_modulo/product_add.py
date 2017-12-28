from osv import fields, osv

class product_add(osv.osv):
    _inherit = 'product.product'

    _columns = {'prueba' : fields.char('Prueba', size=128, translate=True, help='Hola'),
    }

    _defaults = { 'prueba' : 'Estaba vacio, ya no.',
    }
    
product_add()