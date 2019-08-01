# Endless Flighter AI Extravaganza

TensorFlow experiment trying to teach AI to play a simple game.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZmYCy4eH_Mg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Setup instructions

After tinkering with python environment, you should run [Endless Flighter](https://github.com/juhofriman/endless-flighter) game in your browser. Make an setup, in which you can position the game in the same exact location of the screen, as this uses screen capture.

Then adjust these (collect_data.py and run_model.py):

```
screen = np.array(ImageGrab.grab(bbox=(20,220, 420, 450)))
```

to match your environment.

Note: keyboard capturing probably works only on OS X.

## Running

1. Run `collect_data.py`
2. Play the game while running it (20 minutes at least)
3. Run `balance_the_data.py`
4. Run `train_model.py`
5. (Optional) run tensorboard to see the training statistics
6. Run `run_model.py` and set focus to browser running the game
7. If all goes well, it should try to avoid obstacles!

# Credits

This experiment is based mostly on excellent [Python Plays: Grand Theft Auto V](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a) video series.
