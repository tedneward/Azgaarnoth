require "csv"

require "./spell"

module Spellmanager

    class CSVParser
        def initialize(csv : CSV)
            @csv = csv
        end
        def initialize(filepath : String)
            @csv = CSV.new(File.open(filepath), true)
        end

        def next : Bool
            return @csv.next
        end

        def parseSpell : Spell
            title = @csv["Name"]
            source = @csv["Source"]
            level = Spell.parseLevelOrdinal(@csv["Level"])
            castingTime = @csv["Casting Time"]
            duration = @csv["Duration"]
            type = Spell::Type.parse(@csv["School"])
            range = @csv["Range"]
            components = @csv["Components"]
            classes = Spell.parseCaster(@csv["Classes"])
            description = @csv["Text"]
            if @csv["At Higher Levels"] != ""
                description += "\n" + @csv["At Higher Levels"].delete("At Higher Levels.").insert(0, "**At Higher Levels.**")
            end

            ritual = false

            spell = Spell.new(title, level, type, ritual, castingTime, duration, range, components, classes, description, source)
            return spell
        end
    end

    class MDParser
        property lines = Array(String).new

        def initialize(mdFile : File)
            @lines = Array(String).new
            while (str = mdFile.gets) != nil
                @lines << str.as(String)
            end
        end

        def initialize(lines : Array(String))
            @lines = lines
        end

        def parseSpell : Spell
            if lines[0].starts_with?("####")
                return parseWebsiteFormat(lines)
            elsif lines[0].starts_with?("##")
                return parseNewFormat(lines)
            elsif lines[0].starts_with?("#")
                return parseOriginalFormat(lines)
            else
                raise "Not a recognized Spell Markdown format!"
            end
        end

        def parseOriginalFormat(lines : Array(String)) : Spell
            spell = Spell.new

            # "# Alarm"
            spell.title = lines[0].delete("#").strip()

            # "*(2nd-level enchantment)* (Bard, Cleric) (ritual)"

            lines.each do |line|
            end

            return spell
        end
        def parseNewFormat(lines : Array(String)) : Spell
            spell = Spell.new

            spell.title = lines[0].delete("##").strip()

            return spell
        end
        def parseWebsiteFormat(lines : Array(String)) : Spell
            spell = Spell.new

            spell.title = lines[0].delete("####").strip()

            return spell
        end
    end

end
  