class Ex(Exception):
    def __init__(self, text):
        self.text = text

try:
    raise Ex("run away from it")
except Ex as e:
    print("Ex happened - %s" % e)