require "./spec_helper"

require "csv"

describe "Exploration tests" do
    describe "CSV parsing" do
        it "should be able to see the titles of the spells in the test data" do
          csv = CSV.new(File.open("./spec/test.csv"), true)
    
          csv.next
          csv["Name"].should eq("Abi-Dalzim's Horrid Wilting")
    
          csv.next
          csv["Name"].should eq("Absorb Elements")
          
          csv.next
          csv["Name"].should eq("Acid Splash")
        end

        it "should be able to parse a spell from the test data" do
          csv = CSV.new(File.open("./spec/test.csv"), true)
          
          while csv.next
            title = csv["Name"]
            source = csv["Source"]
            level = csv["Level"]
            castingTime = csv["Casting Time"]
            duration = csv["Duration"]
            type = csv["School"]
            range = csv["Range"]
            components = csv["Components"]
            classes = csv["Classes"]
            description = csv["Text"]
            if csv["At Higher Levels"] != ""
                description += "\n" + csv["At Higher Levels"].delete("At Higher Levels.").insert(0, "**At Higher Levels.**")
            end

            spell = Spell.new
            spell.title = title
            spell.source = source
            spell.level = (level.downcase == "cantrip" ? 0 : level[0].to_i)
            spell.type = Spell::Type.parse(type)
            spell.castingTime = castingTime
            spell.duration = duration
            spell.range = range
            spell.components = components
            spell.description = description
          end
      end
    end
end