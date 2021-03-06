# Agent-Based Epidemic Simulation

**Dhilan Chandrasekara** 

Utilizes individual agents to simulate the spread of an infectious virus, then graphs the results. Allows for the changing of simulation parameters such as the total number of agents, agents initially infected, recovery period for the virus and the social distancing factor.

Blue represents individuals never infected, pink represents individuals currently infected and grey represents those who have recovered from the virus.

This simulation shows the high effectiveness of social distancing and self-isolation in 'flattening the curve' associated with viral infections.

![alt text](https://raw.githubusercontent.com/chandrasekara/Agent-Based-Epidemic-Simulation/dev/static/grah3.png "Screenshot of Simulation and Graphed Results")


## Dependencies:

* PyGame
* Matplotlib
* Pandas

To install all relevant dependencies, navigate to root folder and run:

`pip install -r requirements.txt`

## Usage:

`python main.py [-a NUMBER-OF-AGENTS] [-i INITIALLY-INFECTED-NUMBER] [-r RECOVERY-PERIOD] [-d SOCIAL-DISTANCING-FACTOR]`

Alternatively use
`python main.py --default`
to run with default parameters
