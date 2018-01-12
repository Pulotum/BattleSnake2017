# BattleSnake 2017

This is our battlensnake attempt for 2017. It was created by [Me](http://joshlarminay.com) and [AFKMedic](https://github.com/AFKMedic).

The path finding we used for our snake was pretty basic so we decided to name our snake **'Baby Face'**.

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
	- If target square is taken, try up, then try right, then try down, then try left. 
	- If none are possible, go up because we are dead anyways.

### What Can Snake Do Gooder

During the competition, we had some ideas for how to improve the snake slightly without changing the path finding we had. 

* One big problem with out snake was it often defaulted to going up when stuck. This would often result in our snake wrapping into itself or others. We could change it to instead of a compass (north,east,wouth,west) to random movement. This would stop it from cornering itself but would make it a bit more unpredictable and could get it stuck more often because of this.

* One idea was to look ahead by one turn. So basically same thing we did, but also check the target squares for the next move. This would hopefully stop us from cornering our selves into walls.

### Credits

* [Josh Larminay](http://joshlarminay.com)
* [AFKMedic](https://github.com/AFKMedic)

### Tools

* Python (The mightiest of snakes!)
* Heroku
* [BattleSnake](https://www.battlesnake.io/)

