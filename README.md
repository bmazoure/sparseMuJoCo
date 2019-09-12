
## Implementation of __**SparseHumanoid-v2**__ 

Environment used in the papers 

* [Leveraging exploration in off-policy algorithms via normalizing flows (CoRL 2019)](https://arxiv.org/pdf/1905.06893.pdf)
```
 @article{mazoure2019leveraging,
  title={Leveraging exploration in off-policy algorithms via normalizing flows},
  author={Mazoure, Bogdan and Doan, Thang and Durand, Audrey and Hjelm, R Devon and Pineau, Joelle},
  journal={Proceedings of the 3rd Conference on Robot Learning (CoRL 2019)},
  year={2019}
} 

```


### Information about the environment:

* Episode max steps: 1000

* The episode terminates if the agent falls down 

* Reward of +1 is granted if the agent's center of mass (COM) is above a threshold distance (wrt to origin) of 0.6.


### How to use
```python
import gym

env=gym.make("SparseHumanoid-v2")
```

