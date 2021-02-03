import argparse
import sys
import commonmark    # pip install commonmark

class Spell:
        """A simple record type for each spell."""
        def __init__(self):
                # The name of the spell
                self.name = ""
                # Conjuration, evocation, ...
                self.type = ""
                # Cantrip, 1st-level, 2nd-level, ...
                self.level = ""
                # Casting time
                self.casting_time = ""
                # Range of the spell
                self.range = ""
                # V, S, M
                self.components = ""
                # Duration of the spell
                self.duration = ""
                # The classes on which this spell appears
                self.classes = ""
                # The filename containing the spell
                self.filename = ""
                # The source material
                self.source = ""

def parseSpell(spellfile):
        """Parse a file into a Spell object."""
        spell = Spell()
        spell.filename = spellfile
        file = open(spellfile, 'r')
        lines = file.readlines()

        # Look at the first line--if it's a "#", it's my style; if it's "####", it's the
        # downloaded style from the 5e.tools site
        if lines[1] == ' ':
                # My style
        else:
                # Website style

def main():
	argparser = argparse.ArgumentParser(description="Process spells in Markdown format.")
	argparser.add_argument(
	        'infile',
        	nargs="?",
	        type=argparse.FileType('r'),
        	default=sys.stdin,
	        help="Input Markdown file to parse, defaults to STDIN")
	args = argparser.parse_args()
	
	inf = args.infile
	lines = []
	for line in inf:
		lines.append(line)
	data = "".join(lines)

	parser = commonmark.Parser()

	ast = parser.parse(data)
	commonmark.dumpAST(ast)


if __name__ == '__main__':
	main()
