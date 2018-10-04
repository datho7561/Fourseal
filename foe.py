# Author: David Thompson
# Date: 3 Oct, 2018

from entity import Entity

# All entities that are inheritly evil are an instance of this class  
class Foe(Entity):
    
    # OVERRIDE
    def attack(self, entities):

        # Find all the non-foe entities when attacking,
        #  and only allow the foe to attack them, not its own kin

        filteredEntities = []

        for e in entities:
            if (not isinstance(e, Foe)):
                filteredEntities.append(e)

        super().attack(filteredEntities)