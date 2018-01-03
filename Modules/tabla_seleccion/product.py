from osv import osv, fields

class product_product(osv.osv):
    _inherit = 'product.product'

    _columns = {
        'seleccion' : fields.many2one('tabla.seleccion', 'Seleccion Prueba', 
                                      help='Se crea una relacion de este campo hacia \
                                      la tabla tabla.seleccion')
        
    }