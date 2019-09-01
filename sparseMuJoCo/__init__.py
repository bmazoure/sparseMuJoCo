from gym.envs.registration import registry, register, make, spec

# Mujoco
# ----------------------------------------

register(
    id='SparseHalfCheetah-v2',
    entry_point='sparseMuJoCo.envs.mujoco:HalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='SparseHalfCheetah-v3',
    entry_point='sparseMuJoCo.envs.mujoco.half_cheetah_v3:HalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='SparseHopper-v2',
    entry_point='sparseMuJoCo.envs.mujoco:HopperEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='SparseHopper-v3',
    entry_point='sparseMuJoCo.envs.mujoco.hopper_v3:HopperEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='SparseSwimmer-v2',
    entry_point='sparseMuJoCo.envs.mujoco:SwimmerEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='SparseSwimmer-v3',
    entry_point='sparseMuJoCo.envs.mujoco.swimmer_v3:SwimmerEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='SparseWalker2d-v2',
    max_episode_steps=1000,
    entry_point='sparseMuJoCo.envs.mujoco:Walker2dEnv',
)

register(
    id='SparseWalker2d-v3',
    max_episode_steps=1000,
    entry_point='sparseMuJoCo.envs.mujoco.walker2d_v3:Walker2dEnv',
)

register(
    id='SparseAnt-v2',
    entry_point='sparseMuJoCo.envs.mujoco:AntEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='SparseAnt-v3',
    entry_point='sparseMuJoCo.envs.mujoco.ant_v3:AntEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='SparseHumanoid-v2',
    entry_point='sparseMuJoCo.envs.mujoco:HumanoidEnv',
    max_episode_steps=1000,
)

register(
    id='SparseHumanoid-v3',
    entry_point='sparseMuJoCo.envs.mujoco.humanoid_v3:HumanoidEnv',
    max_episode_steps=1000,
)

register(
    id='SparseHumanoidStandup-v2',
    entry_point='sparseMuJoCo.envs.mujoco:HumanoidStandupEnv',
    max_episode_steps=1000,
)
