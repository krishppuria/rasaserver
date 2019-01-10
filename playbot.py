from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

def run(namevalue,serve_forever=True):
    interpreter = RasaNLUInterpreter("./models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interprete)
    #print("Your bot is ready to talk! Type your messages here or send 'stop'")
    #while
    responses = agent.handle_text(namevalue)
    return responses


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")
    run()
