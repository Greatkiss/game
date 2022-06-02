import pandas as pd
import random

class map:
	def __init__(self):
		self.map = pd.read_csv("map.csv").fillna('')
		#self.map = self.map['Price'].astype(int)
		#self.map = self.map['Fee'].astype(int)
	def change_owner(self,num,pname):
		place = self.map["Name"][num]
		self.map.at[place,"Owner"]=pname

class player:
	def __init__(self,name):
		self.pname = name
		self.money=1000
		self.pos=0
		self.rent=0
		self.jailcount=0
	
	def turn(self):
		print("its {}'s turn".format(self.pname))
		while True:
			print("roll the dice and move : 1")
			print("negosiation : 2")
			print("others : 3")
			try:
				action = int(input())
				break
			except:
				print("type the correct option")
		if action == 1:
			self.move(map.map,map)
		elif action == 2:
			print("")
		elif action == 3:
			print("")
		else:
			print("error")

	def pay(self,you,much):
		#deal with self money
		if self.money == 0:
			self.rent += much
		#error exception
		elif self.money<0:
			print("error at {}s money".format(self.pname))
		#transaction
		else:
			self.money -= much
			print("you paid {} to {}".format(much, you.pname))
		if you.rent > 0:
			if you.rent > much:
				you.rent -= much
			else:
				you.money = you.money + much - you.rent
				you.rent = 0
		else:
			you.money += much
		
	def move(self,map,mapclass):
		print("{} roll deces".format(self.pname))
		many = random.randint(1,12)
		print("the result of the roll is {}".format(many))
		self.pos += many
		#error exception
		if self.pos < 0:
			print("error at {}s position".format(self.pname))
		elif self.pos > 39:
			self.pos -= 40
		#event
		print("{}".format(map['Name'][self.pos]))
		if map['Name'][self.pos] == 'GO':
			self.money += 400
		elif map['Name'][self.pos] == '共同基金':
			print("")
		elif map['Name'][self.pos] == '刑務所':
			if self.jailcount > 0:
				self.jailcount -= 1
				print("your jail count is {}".format(self.jailcount))
		elif map['Name'][self.pos] == 'GO TO JAIL':
			self.pos = 10
			print("you are in jail")
			self.jailcount = 3
		elif map['Name'][self.pos] == 'チャンス':
			print("")
		#buy the land
		else:
			if map["Owner"][self.pos] != '':
				if map["Owner"][self.pos] != self.pname:
					self.pay(map["Owner"][self.pos],map["Fee"][self.pos])
			else:
				print('you can buy this place :  {} with {}'.format(map["Name"][self.pos],map["Price"][self.pos]))
				while True:
					print("if {} want to buy this place, enter y".format(self.pname))
					ans = input()
					if ans == 'y':
						mapclass.map["Owner"][self.pos] = self.pname
						break
					else:
						print("you will miss the buy chance. Are you sure??? y/n")
						reans = input()
						if reans == 'y':
							break
						else:
							continue
			
if __name__ == "__main__":
	map = map()
	p1 = player("kaneko")
	p2 = player("ayaka")
	i = 0
	while i < 10:
		p1.turn()
		p2.turn()
		i+=1