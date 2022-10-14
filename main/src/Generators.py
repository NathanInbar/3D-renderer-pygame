from typing import Tuple
from random import randrange

class _RandomColorGen():

    def __init__(self,step=1):
        self.gen = self._randomColorGen(step)

    def _randomColorGen(self,step):
        while True:
            yield (randrange(10,240,step),randrange(10,240,step),randrange(10,240,step))

    def getNext(self) -> Tuple[int,int,int]:
        return next(self.gen)

RandomColorGen = _RandomColorGen() #singleton