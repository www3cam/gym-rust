from gym.envs.registration import register

register(
    id='RustEnv-v0',
    entry_point='gym_rust.envs:RustEnv',
)
