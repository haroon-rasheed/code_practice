

class LoadUTErrorBase(Exception):
	def __init__(self, err_type, component):
		self.err_type = err_type
		self.component = component

	def __str__ (self):
		if (self.err_type == IOError ):
			err_msg = "Lookup Failure, check whether these files/dirs %s exist(s)" %(self.component)
			return repr(err_msg)
