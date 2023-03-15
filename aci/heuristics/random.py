import torch as th
import numpy as np

class RandomAgent:
    def __init__(self, observation_shape, n_actions, device, **_):
        self.n_actions = n_actions
        self.device = device

    def get_q(self, actions, **_):
        q = th.rand((*actions.shape[:3], self.n_actions), device=self.device)
        return q


class FixedAgent:
    def __init__(self, observation_shape, n_actions, n_nodes, device, **_):
        self.n_actions = n_actions
        self.device = device
        self.q = th.rand((n_nodes, n_actions), device=self.device)

    def get_q(self, actions, **_):
        q = self.q[np.newaxis,np.newaxis].expand(actions.shape[0],actions.shape[1],-1,-1)
        return q
