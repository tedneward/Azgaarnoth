module Spellmanager
    class Spell
        enum Type
            None
            Abjuration
            Conjuration
            Divination
            Enchantment
            Evocation
            Illusion
            Necromancy
            Transmutation

            def to_s
                return super.downcase
            end
        end

        enum Caster
            Artificer
            Bard
            Cleric
            Druid
            Paladin
            PaleMaster
            Ranger
            Sorcerer
            Warlock
            Wizard
        end
        
        def self.parseCaster(str : String)
            casterArray = [] of Caster

            if str == ""
                return casterArray
            end

            strArray = str.split(",")
            strArray.each do |el|
                elem = el.strip(" ")
                if elem == "Artificer (Revisited)"
                    casterArray << Caster::Artificer
                else
                    casterArray << Caster.parse(elem)
                end
            end
            return casterArray.uniq()
        end

        property title : String = ""
        property level : Int32 = -1
        property type : Type = Type::None
        property ritual : Bool = false
        property castingTime : String = ""
        property duration : String = ""
        property range : String = ""
        property components : String = ""
        property classes = [] of Caster
        property description : String = ""
        property source : String = ""

        def initialize(title : String, level : Int32, type : Type, ritual : Bool, 
                ct : String, d : String, r : String, comp : String, 
                classes : Array(Caster), desc : String, source = "")
            @title = title
            @level = level
            @type = type
            @ritual = ritual
            @castingTime = ct
            @duration = d
            @range = r
            @components = comp
            @classes = classes.sort
            @description = desc
            @source = source
        end

        def initialize()
        end

        def leveled
            case @level
                when 1
                    return "1st"
                when 2
                    return "2nd"
                when 3
                    return "3rd"
                when 4
                    return "4th"
                when 5
                    return "5th"
                when 6
                    return "6th"
                when 7
                    return "7th"
                when 8
                    return "8th"
                when 9
                    return "9th"
                else
                    return "WTF?!?!"
            end
        end
        def self.parseLevelOrdinal(str : String) : Int32
            case str
            when "Cantrip"
                return 0
            when "1st"
                return 1
            when "2nd"
                return 2
            when "3rd"
                return 3
            when "4th"
                return 4
            when "5th"
                return 5
            when "6th"
                return 6
            when "7th"
                return 7
            when "8th"
                return 8
            when "9th"
                return 9
            else
                return -1
            end
        end

        def ritualized
            return @ritual ? " (ritual)" : ""
        end

        def classList
            str = ""
            @classes.each do |elem|
                str = str + elem.to_s + ", "
            end
            return str.rchop.rchop
        end

        # The formatting should look like:
        # ## Alarm
        # *1st-level abjuration (ritual)*
        # ____
        # - **Classes:** Bard, Sorcerer, Wizard
        # - **Casting Time:** 1 minute
        # - **Range:** 30 feet
        # - **Components:** V, S, M (blah)
        # - **Duration:** 8 hours
        # ---
        # Descriptive text
        #
        # *(Source: )*
        def to_md
            # Title
            mdText = "## #{@title}\n"

            # Descriptor
            if @level == 0
                mdText = mdText + "*#{@type} cantrip#{ritualized}*\n"
            else
                mdText = mdText + "*#{leveled}-level #{@type}#{ritualized}*\n"
            end

            # Separator
            mdText = mdText + "____\n"

            # Classes
            mdText = mdText + "**Classes:** #{classList}\n"

            # Casting Time
            mdText = mdText + "**Casting Time:** #{@castingTime}\n"

            # Range
            mdText = mdText + "**Range:** #{@range}\n"

            # Components
            mdText = mdText + "**Components:** #{@components}\n"

            # Duration
            mdText = mdText + "**Duration:** #{@duration}\n"

            # Separator
            mdText = mdText + "____\n"

            # Description
            mdText = mdText + @description + "\n"

            # Source
            mdText = mdText + "\n*(Source: #{@source != "" ? @source : "(Unknown)"})*\n"

            return mdText
        end

    end
  
end
