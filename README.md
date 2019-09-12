
## Implementation of __**SparseHumanoid-v2**__ 

Environment used in the paper 

* [Leveraging exploration in off-policy algorithms via normalizing flows](https://arxiv.org/pdf/1905.06893.pdf)
### Information about the environment:

* Episode max steps: 1000

* The episode terminates if the agent falls down 

* Reward of +1 is granted if the agent's center of mass (COM) is above a threshold distance (wrt to origin) of 0.6.


### How to use
```python
import gym

env=gym.make("SparseHumanoid-v2")
```


To cite the paper:
