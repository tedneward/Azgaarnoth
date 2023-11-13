name = 'Rage Mage'
description = "***Primal Path: Path of the Rage Mage.*** A rage mage taps into the primal essence of magic, using her own natural anger and frenzy to channel the arcane power in flashy, flamboyant ways. Like any barbarian, a rage mage is often the product of a less civilized society. A rage mage is not necessarily stupid, however, and should be feared for it."
class RageMageSpellcasting(Spellcasting):
    def __init__(self, npc):
        Spellcasting.__init__(self, npc, 'CHA', "Rage Mage Spellcasting")
        self.casterclass = allclasses['Barbarian']
        del self.maxcantripsknown
        del self.maxspellsknown

    def maxcantripsknown(self):
        npc = self.npc
        return 2 if npc.levels('Barbarian') < 10 else 3

    def maxspellsknown(self):
        npc = self.npc
        return 3 if npc.levels('Barbarian') < 4 else 4 if npc.levels('Barbarian') < 7 else 5 if npc.levels('Barbarian') < 8 else 6 if npc.levels('Barbarian') < 10 else 7 if npc.levels('Barbarian') < 11 else 8 if npc.levels('Barbarian') < 13 else 9 if npc.levels('Barbarian') < 14 else 10 if npc.levels('Barbarian') < 16 else 11 if npc.levels('Barbarian') < 19 else 12 if npc.levels('Barbarian') < 20 else 13

    def furypoints(self):
        npc = self.npc
        return 4 if npc.levels('Barbarian') < 4 else 6 if npc.levels('Barbarian') < 7 else 14 if npc.levels('Barbarian') < 10 else 17 if npc.levels('Barbarian') < 13 else 27 if npc.levels('Barbarian') < 16 else 32 if npc.levels('Barbarian') < 19 else 38

    def emitMD(self):
        text = f">***Rage Mage Spellcasting (Cha, at level {self.casterlevel()}. Recharges on long rest).*** "
        text += f"Spell save DC: {self.spellsavedc()}, Spell attack bonus: +{self.spellattack()} "
        text += f"{self.furypoints()} Fury Points. "
        text += f"{self.maxcantripsknown()} cantrips known. "
        text += f"{self.maxspellsknown()} spells known.\n"
        text += f">\n>Cantrips known:\n"
        text +=  ">\n>Spells known:\n"
        text += f">* *1st-level (2 fury points):*\n"
        if self.npc.levels('Barbarian') >= 7: text += f">* *2nd-level (3 fury points):*\n"
        if self.npc.levels('Barbarian') >= 13: text += f">* *3rd-level (5 fury points):*\n"
        if self.npc.levels('Barbarian') >= 19: text += f">* *4th-level (6 fury points):*\n"
        text +=  ">\n"
        return text

def level3(npc):
    npc.traits.append("***Font of Fury.*** When you cast a spell while raging, attack rolls against you are rolled with advantage until the beginning of your next turn. In addition, your rage ends early if you are knocked unconscious, if your turn ends and you haven't attacked a hostile creature, cast a spell, or taken damage since the end of your previous turn. Otherwise your rage works normally.")
    npc.spellcasting['Rage Mage Spellcasting'] = RageMageSpellcasting(npc)
