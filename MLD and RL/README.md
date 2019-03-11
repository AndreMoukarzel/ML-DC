# Value Iteration

python gridworld.py -a value -i 5

# Q-Learning

python gridworld.py -a q -k 100
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid

# Q-Learning with features

python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60
-l mediumGrid
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60
-l mediumClassic