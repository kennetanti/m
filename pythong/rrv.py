from rethinkdb import RethinkDB
r = RethinkDB()
from threading import Thread

r.set_loop_type("asyncio")

class reModel:
	db_name="na"
	table_name="na"
	
	async def table(s):
		return r.db(s.db_name).table(s.table_name)
	
	async def feed(s): 
		return s.table().changes(include_initial=True).run(await s.con)
	async def push(s,d):
		return s.table().insert(d).run(await s.con)
	async def delete(s,w):
		return s.table().filter(w).delete().run(await s.con)
	
	async def dbs(s):
		return r.db_list().run(await s.con)
	async def db_add(s):
		return r.db_create(s.db_name).run(await s.con)
	async def tables(s):
		return r.db(s.db_name).table_list().run(await s.con)
	async def table_add(s):
		return r.db(s.db_name).table_create(s.table_name).run(await s.con)
	
	def __init__(s, host="rvdb", port=28015):
		s.asyncinit(host, port)
	async def asyncinit(s,host,port):
		s.con = r.connect(host=host, port=port)
		if s.db_name not in await s.dbs():
			await s.db_add()
		if s.table_name not in await s.tables():
			await s.table_add()
		
class reJob(reModel):
	db_name="rejobs"
	
	def __init__(self, job_name):
		self.table_name = job_name
		reModel.__init__(self)
		
class reAct(Thread):
	from_model = None
	to_model = None
	job_name = "na"
	
	def __init__(self):
		self.init_jobmodel()
		Thread.__init__(self)
	def run(self):
		self.asyncrun(self)
	async def asyncrun(self):
		async for change in self.from_model.feed():
			row = change["new_val"]
			if self.try_claim(row["id"]):
				self.proc(row)
	def proc(self, data):
		raise NotImplementedException
	def init_jobmodel(self):
		self.job_model = reJob(self.job_name)
	def try_claim(self, ident):
		ret = self.job_model.push({"id": ident})
		return ret["inserted"] > 0
