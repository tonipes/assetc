import logging as logger
import json

from .action import all_action_types

def unpack(l):
    return [i for s in l for i in s]

def action_decoder(obj):
    if 'type' in obj:
        matches = list(filter(lambda t: t.name == obj['type'], all_action_types))

        if not matches:
            logger.error("No action of type " + obj['type'] + " found")
        
        return matches[0](**obj)

    return obj

class Config(object):
    def __init__(self, raw, platform="unknown"):
        parsed = json.loads(raw, object_hook=action_decoder)
        self.actions = parsed["actions"]

        self.globals = parsed["globals"]["default"]

        if platform in parsed["globals"]:
            dict.update(self.globals, parsed["globals"][platform])

        self.post_build_actions = parsed["post_build_actions"]

        self.globs = unpack([action.globs for action in self.actions])