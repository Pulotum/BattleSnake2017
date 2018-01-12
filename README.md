# BattleSnake 2017

This is our battlensnake attempt for 2017. It was created by Me and [AFKMedic](https://github.com/AFKMedic). 

#### How Our Snake Do

So our snake design was pretty basic all things considered. It's goal was to get to the closest food.
The steps it followed are pretty basic.

1) Get the head's location and compare it to the food locations. Make the closet food object the next target.

2) Figuring out if the food is higher or lower than the snake on the board.

3) If it's higher, move up by one. If it's lower, move down by one.

4) Repeat this until we are at the same level as the food.

5) Repeat the same steps except for left and right.

6) During this, we check the next spot w are aiming for to see if a snake is there.

7) If there is a snake, we default to the first available space in a compass fashion.
*If target square is taken, try up, then try right, then try down, then try left.
*If none are possible, go up because we are dead anyways.


It accomplished this by comparing it's head coordinates and coparing it to all the food objects. This will find the cloests one.

* a working Python 2.7 development environment ([getting started guide](http://hackercodex.com/guide/python-development-environment-on-mac-osx/))
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

## Running the Snake Locally

1) [Fork this repo](https://github.com/sendwithus/battlesnake-python/fork).

2) Clone repo to your development environment:
```
git clone git@github.com:username/battlesnake-python.git
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
python app/main.py
```

5) Test client in your browser: [http://localhost:8080](http://localhost:8080).

## Deploying to Heroku

1) Create a new Heroku app:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command:
```
heroku logs --tail
```

## Questions?

Email [battlesnake@sendwithus.com](mailto:battlesnake@sendwithus.com), or tweet [@send_with_us](http://twitter.com/send_with_us).
