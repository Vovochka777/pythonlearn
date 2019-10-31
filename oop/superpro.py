class Robot(object):
    'class that move robot'
    def fetch(self, tool):
        print 'Grab the tool'

    def replace(self, tool):
        print 'Replace the tool'

class CleaningRobot(Robot):

    def clean(self, tool):
        super(CleaningRobot, self).fetch(tool)
        print 'left right left'
        super(CleaningRobot, self).replace(tool)



class EmulateRobot(Robot):
    def fetch(self, tool):
        print 'Emulate grab the tool'

    def replace(self, tool):
        print 'Emulate replace the tool'

class EmulateCleaningRobot(CleaningRobot, EmulateRobot):
    'empty '

emulator = EmulateCleaningRobot()
emulator.clean("broom")