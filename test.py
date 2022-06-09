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

class cards:
	def __init__(self):
		self.com_cards = pd.read_csv("com_cards.csv")
		self.cha_cards = pd.read_csv("cha_cards.csv")
	def draw(self,card_type):
		print("You draw a {} card".format(card_type))
		if card_type == "共同基金":
			print("You draw a {} card".format(card_type))
			n = random.randint(1,15)
			print("".format(self.com_cards['Name'][n]))
		elif card_type == "チャンス":
			print("You draw a {} card".format(card_type))
    		

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
			print("move : 1")
			print("pay : 2")
			try:
				action = int(input())
				break
			except:
				print("type the correct option")
		if action == 1:
			self.move(map.map,map,cards)
		elif action == 2:
			while True:
				print("who do you want to pay?")
				you = input()
				print("how much do you want to pay?")
				much = input()
				print("So, you will pay {} to {}. (y/n)".format(much, you))
				ans = input()
				if ans == 'y':
					break
				else:
					continue
			self.pay(you,much)
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
		
	def move(self,map,mapclass,cardclass):
		print("Your movement is 1:Roll dices, 2:Card")
		ans = input()
		if ans == "1":
			many = self.roll_dice()
			self.pos += many
		elif ans == "2":
			while True:
				print(map)
				print("Type the position number of the place")
				try:
					dest = int(input())
				except:
					dest = 0
				print("You are going to {}. Are you sure? (y/n)".format(map['Name'][dest]))
				ans = input()
				if ans == 'y':
					break
				else:
					continue
			self.pos = dest
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
			cardclass.draw('共同基金')
		elif map['Name'][self.pos] == '刑務所':
			if self.jailcount > 0:
				self.jailcount -= 1
				print("your jail count is {}".format(self.jailcount))
		elif map['Name'][self.pos] == 'GO TO JAIL':
			self.pos = 10
			print("you are in jail")
			self.jailcount = 3
		elif map['Name'][self.pos] == 'チャンス':
			cardclass.draw('チャンス')
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
	def roll_dice(self):
		print("{} roll deces".format(self.pname))
		many = random.randint(1,12)
		print("the result of the roll is {}".format(many))
		return many


if __name__ == "__main__":
	map = map()
	cards = cards()
	p1 = player("kaneko")
	p2 = player("ayaka")
	i = 0
	while i < 10:
		while True:
			p1.turn()
			print("are you done? (y/n)")
			ans = input()
			if ans == 'y':
				break
			else:
				continue
		while True:
			p2.turn()
			print("are you done? (y/n)")
			ans = input()
			if ans == 'y':
				break
			else:
				continue
		i+=1