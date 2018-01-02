from osv import osv, fields

class events(osv.osv):
	
	def calcutateEndDate(dateString, length):
		pass

	_name = 'project.events'

	_columns = {
		'name': fields.char('Nombre', size=120, required=True),
		'description': fields.text('Descripcion', required=True),
		'startdate': fields.date('Fecha Inicio', required=True), 
		'length': fields.integer('Duracion', size=10, required =True, help='Expresar la cantidad de dias'),
		'costamount': fields.float('Costo', required=True), 
	}

	_order = 'name'

events()
