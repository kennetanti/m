import rrv

class testone(rrv.reModel):
	db_name = "boop"
	table_name = "beep"

class testtwo(rrv.reModel):
	db_name = "blurp"
	table_name = "blap"

class do_thing(rrv.reAct):
	from_model = testone()
	to_model = testtwo()
	job_name = "thing"
	
	def proc(self, data):
		print repr(data)
		data["thaaang"] = data["thang"]*2
		self.to_model.push(data)

class do_thang(rrv.reAct):
	from_model = testtwo()
	to_model = None
	job_name = "thaaang"
	
	def proc(self, data):
		print repr(data)
		
thang = do_thing()
thang.start()
thaang = do_thang()
thaang.start()


import time
time.sleep(1)
t1 = testone()

for x in range(100):
	t1.push({"thang": x})
	time.sleep(1)
