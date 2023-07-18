from actions.appliance import Appliance
from command_abc import AbsCommand


class ApplianceOnCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError(f'Expected a Appliance object, got {appliance.__class__.__name__} instead.')
        self.appliance = appliance

    def execute(self):
        self.appliance.on()

    def undo(self):
        self.appliance.off()


class ApplianceOffCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError(f'Expected a Appliance object, got {appliance.__class__.__name__} instead.')
        self.appliance = appliance

    def execute(self):
        self.appliance.off()

    def undo(self):
        self.appliance.on()