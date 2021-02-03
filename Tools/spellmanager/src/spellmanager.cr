require "option_parser"

require "./spell"
require "./parser"

# TODO: Write documentation for `Spellmanager`
module Spellmanager
  VERSION = "0.1.0"
end

include Spellmanager

optionsparser = OptionParser.parse do |parser|
  parser.banner = "Usage: spellmanager [arguments]"
  parser.on "-v", "--version", "Show the version" do
    puts "spellmanager {Spellmanager::VERSION}"
  end
  parser.on "-h", "--help", "Show this help" do
    puts parser
  end
  parser.on "-c FILE", "--csv=FILE", "Input: Parse a CSV file" do |file|
    csvparser = CSVParser.new(file)
    while csvparser.next
      puts csvparser.parseSpell().to_md
    end
  end
  parser.on "-i FILE", "--input=FILE", "Input: Markdown file to parse" do |file|
    mdParser = MDParser.new(File.open(file))
    spell = mdParser.parseSpell
    puts spell.to_md
  end
  parser.on "-s DIR", "--source=DIR", "Input: Parse a directory of existing markdown files" do |dir|
    Dir.each(dir) do |node|
      puts node
    end
  end
  parser.on "-o FILE", "--outDB=FILE", "Output: SQLite database in to which to write output" do |dbfile|

  end
  parser.on "-t DIR", "--target=DIR", "Output: Directory into which to write output" do |dir|

  end
end
