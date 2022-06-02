import pandas as pd

class map:
	def __init__(self):
		#map = pd.read_csv("map.csv")
		self.map = pd.DataFrame([["aaa",100,10,""],["bbb",200,20,""]], columns = ["Name", "Price", "Fee","Owner"])
	def change_owner(self,num,pname):
		place = self.map["Name"][num]
		self.map.at[place,"Owner"]=pname

class player:
	def __init__(self,name):
		self.pname = name
		self.money=1000
		self.pos=0
		self.rent=0

	def pay(self,you,much):
		#deal with self money
		if self.money == 0:
			self.rent += much
		elif self.money<0:
			print(f"error at {pname}'s money")
		else:
			self.money -= much
		#deal with your money
		if you.rent > 0:
			if you.rent > much:
				you.rent -= much
			else:
				you.money = you.money + much - you.rent
				you.rent = 0
		else:
			you.money += much
		
	def move(self,many,map):
		self.pos += many
		if self.pos < 0:
			print(f"error at {pname}'s position")
		elif self.pos > 39:
			self.pos -= 40
		if map["Owner"][self.pos] is not None:
			if map["Owner"][self.pos] is not self.pname:
				self.pay(map["Owner"][self.pos],map["Fee"][self.pos])
		else:
			print(f'you can buy this place :  {map["Name"][self.pos]} with {map["Price"][self.pos]}')
			print("if you want to buy this place, enter y")
			ans = input()
			if ans == 'y':
				map["Owner"][self.pos] == self.pname

if __name__ == "__main__":
	map = map()
	p1 = player("kaneko")
	print(map.map["Owner"][p1.pos])
	p1.move(1,map)