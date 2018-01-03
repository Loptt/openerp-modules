from osv import osv, fields

class tabla_seleccion(osv.osv):

    _name = 'tabla.seleccion'

    _columns = {
        'name' : fields.char('Nombre', size=100),
        'number' : fields.integer('Numero', size=10),
        'description' : fields.text('Descripcion')
    }
