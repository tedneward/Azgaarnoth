require "./spec_helper"

include Spellmanager

describe Spellmanager do
  describe "Spell Enums" do
    it "should parse conjuration correctly" do 
      Spell::Type.parse("conjuration").should eq(Spell::Type::Conjuration)
    end

    it "should raise an exception for an unknown type" do
      expect_raises(Exception, "unknown") do
        Spell::Type.parse("unknown")
      end
    end

    it "should parse Artificer" do
      Spell.parseCaster("Artificer")[0].should eq(Spell::Caster::Artificer)
    end
    it "should parse Artificer (Revisited) as Artificer" do
      Spell.parseCaster("Artificer (Revisited)")[0].should eq(Spell::Caster::Artificer)
    end
  end

  describe "Spell Markdown Input Parser" do
    def validateZOTSpell(spell)
      spell.title.should eq("Zone of Truth")
      #spell.level.should eq(2)
      #spell.type.should eq(Spell::Type::Enchantment)
    end

    it "should parse the final markdown format successflly" do
      zone_of_truth = 
      <<-SPELL
      ## Zone of Truth
      *2nd-level enchantment*
      ____
      **Classes:** Bard, Cleric, Paladin
      **Casting Time:** Action
      **Range:** 60 feet
      **Components:** V, S
      **Duration:** 10 minutes
      ____
      You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there must make a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its saving throw.An affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in its answers as long as it remains within the boundaries of the truth.
          
      *(Source: PHB)*"
      SPELL
      mdParser = MDParser.new(zone_of_truth.split("\n"))
      spell = mdParser.parseSpell()
      validateZOTSpell(spell)
    end

    it "should parse my original markdown format successfully" do
      zone_of_truth = 
      <<-SPELL
      # Zone of Truth
      *2nd-level enchantment* (Bard, Cleric, Paladin)
      
      **Casting Time:** Action

      **Range:** 60 feet

      **Components:** V, S

      **Duration:** 10 minutes

      You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there must make a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its saving throw.An affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in its answers as long as it remains within the boundaries of the truth.
          
      *(Source: PHB)*"
      SPELL
      mdParser = MDParser.new(zone_of_truth.split("\n"))
      spell = mdParser.parseSpell()
      validateZOTSpell(spell)
    end

    it "should parse the website markdown format successfully" do
      zone_of_truth = 
      <<-SPELL
      #### Zone of Truth
      *2nd-level enchantment*
      ___
      - **Casting Time:** 1 action
      - **Range:** 60 feet
      - **Components:** V, S
      - **Duration:** 10 minutes
      ---
      You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there must make a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its saving throw.
      
      An affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in its answers as long as it remains within the boundaries of the truth
      SPELL
      mdParser = MDParser.new(zone_of_truth.split("\n"))
      spell = mdParser.parseSpell()
      validateZOTSpell(spell)
    end

    it "should parse an MD file in the website format" do
      mdParser = MDParser.new(File.open("./spec/alarm.md"))
      spell = mdParser.parseSpell()
      spell.title.should eq("Alarm")
    end
  end

  describe "Spell markdown output" do
    arcane = [Spell::Caster::Sorcerer, Spell::Caster::Warlock, Spell::Caster::Wizard]
    divine = [Spell::Caster::Cleric, Spell::Caster::Paladin]
    nature = [Spell::Caster::Druid, Spell::Caster::Ranger]

    acid_splash = Spell.new("Acid Splash", 0, Spell::Type::Conjuration, false, 
      "1 minute", "8 hours", "30 feet", "V, S, M (a tiny bell)",  
      arcane,
      "Description...", "PHB")
    alarm = Spell.new("Alarm", 1, Spell::Type::Abjuration, true, 
      "1 minute", "8 hours", "30 feet", "V, S, M (a tiny bell)", 
      arcane + nature,
      "Description...")

    it "should return correct title and descriptor for a cantrip" do
      acid_splash.to_md.should contain("## Acid Splash\n*conjuration cantrip*\n")
      acid_splash.to_md.should contain("Sorcerer, Warlock, Wizard")
      acid_splash.to_md.should contain("**Casting Time:** 1 minute")
      acid_splash.to_md.should contain("**Range:** 30 feet")
      acid_splash.to_md.should contain("**Duration:** 8 hours")
      acid_splash.to_md.should contain("**Components:** V, S, M")
    end
    it "should return correct title and descriptor for a non-cantrip" do
      alarm.to_md.should contain("## Alarm\n*1st-level abjuration (ritual)*\n")
      alarm.to_md.should contain("Druid, Ranger, Sorcerer, Warlock, Wizard")
      alarm.to_md.should contain("**Casting Time:** 1 minute")
      alarm.to_md.should contain("**Range:** 30 feet")
      alarm.to_md.should contain("**Duration:** 8 hours")
      alarm.to_md.should contain("**Components:** V, S, M")
    end
  end

end
