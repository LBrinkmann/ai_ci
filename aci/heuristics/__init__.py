# from .agent import HeuristicAgent1
# from .ai import HeuristicAI1
# from .titfortat import TitForTat
from .random import RandomAgent, FixedAgent


HEURISTICS = {
    "random": RandomAgent,
    'fixed': FixedAgent
}
