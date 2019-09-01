from gym.envs.mujoco.mujoco_env import MujocoEnv
# ^^^^^ so that user gets the correct error
# message if mujoco is not installed correctly
from sparseMuJoCo.envs.mujoco.ant import AntEnv
from sparseMuJoCo.envs.mujoco.half_cheetah import HalfCheetahEnv
from sparseMuJoCo.envs.mujoco.hopper import HopperEnv
from sparseMuJoCo.envs.mujoco.walker2d import Walker2dEnv
from sparseMuJoCo.envs.mujoco.humanoid import HumanoidEnv
from sparseMuJoCo.envs.mujoco.humanoidstandup import HumanoidStandupEnv
