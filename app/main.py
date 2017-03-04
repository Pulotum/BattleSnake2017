import bottle
import os
import random
import math

def isDangerSquare(data, next):
	dangers = []
	
	snakes = data["snakes"]
	
	for snake in snakes:
		curds = snake["coords"]
		for cord in curds:
			dangers.append(cord)
        #area around enemy snake head
        if snake["id"] != data["you"]
            head = snake["coords"][0]
            #right
            dangers.append([head[0] + 1, head[1])
            #left
            dangers.append([head[0] - 1, head[1])
            #up
            dangers.append([head[0], head[1] - 1])
            #down
		    dangers.append([head[0], head[1] + 1])
	print dangers
	
	if( next in dangers):
		print "square taken"
		return true;

def getTaunt():
	taunts = [	'This is a taunt!',
				'Woot taunt']
				
	return random.choice(taunts)

@bottle.route('/static/<path:path>')
def static(path):
	return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():

	data = bottle.request.json
	game_id = data['game_id']
	board_width = data['width']
	board_height = data['height']

	head_url = 'https://thumb1.shutterstock.com/display_pic_with_logo/88356/107460737/stock-photo-beautiful-expressive-adorable-happy-cute-laughing-smiling-baby-infant-face-showing-tongue-isolated-107460737.jpg'
	
	# TODO: Do things with data

	return {
		'color': '#ff6666',
		'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
		'head_url': head_url,
		'name': 'Baby Face',
		'head_type': 'safe',
		'tail_type': 'pixel'
	}

	

@bottle.post('/move')
def move():
	global closeFood
	
	data = bottle.request.json
	
	uid = data["you"]
	snakes = data["snakes"]
	
	for snek in snakes:
		if(snek["id"] == uid):
			me = snek
		
	meX = me["coords"][0][0]
	meY = me["coords"][0][1]
	
	closestCord = []
	closestDistX = 100
	closestDistY = 100
	
	for item in data["food"]:
		currentX = abs(meX - item[0])
		currentY = abs(meY - item[1])
		
		if((currentX < closestDistX) and (currentY < closestDistY)):
			closestDistX = currentX
			closestDistY = currentY
			closestCord = item
		
	print "me -", meX, meY)
	print "closestCord -", closestCord
	
	isGood = False
	while (isGood == False):
		if((closestCord[0] < meX) and (lockRight == False)):
			movement = 'right'
			wantedSquare = [meX + 1, meY]
		elif((closestCord[0] > meX) and (lockLeft == False)):
			movement = 'left'
			wantedSquare = [meX - 1, meY]
		elif((closestCord[1] > meY) and (lockDown == False)):
			movement = 'down'
			wantedSquare = [meX, meY + 1]
		elif((closestCord[1] < meY) and (lockUp == False)):
			movement = 'up'
			wantedSquare = [meX, meY - 1]
	
		print "wanted movement -", movement
		
		isGood = isDangerSquare(data, wantedSquare)
		
		print "isGood -", isGood
		
		if(isGood == False):
			if(movement == 'right'):
				lockRight = True
			elif(movement == 'left'):
				lockLeft = True
			elif(movement == 'down'):
				lockDown = True
			elif(movement == 'up'):
				lockUp = True
		
		print "Next Check -------"
		
	
	# TODO: Do things with data	
	
	return {
		'move': nextMove,
		'taunt': getTaunt()
	}
	
@bottle.post('/end')
def end():
	data = bottle.request.json

	# TODO: Do things with data

	return {
		'taunt': 'BABY FACE!'
	}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
	bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
