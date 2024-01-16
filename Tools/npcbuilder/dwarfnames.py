import random

def generate_name(exemplars):
    chain = markov_chain(exemplars)
    if chain:
        return markov_name(chain)
    return ''

def markov_name(chain):
    parts = select_link(chain, 'parts')
    names = []
    for _ in range(parts):
        name_len = select_link(chain, 'name_len')
        c = select_link(chain, 'initial')
        name = c
        last_c = c
        while len(name) < name_len:
            c = select_link(chain, last_c)
            if not c:
                break
            name += c
            last_c = c
        names.append(name)
    return ' '.join(names)

def markov_chain(names):
    return construct_chain(names)

def construct_chain(lst):
    chain = {}
    for item in lst:
        names = item.split()
        chain = incr_chain(chain, 'parts', len(names))
        for name in names:
            chain = incr_chain(chain, 'name_len', len(name))
            c = name[0]
            chain = incr_chain(chain, 'initial', c)
            string = name[1:]
            last_c = c
            while len(string) > 0:
                c = string[0]
                chain = incr_chain(chain, last_c, c)
                string = string[1:]
                last_c = c
    return scale_chain(chain)

def incr_chain(chain, key, token):
    if key in chain:
        if token in chain[key]:
            chain[key][token] += 1
        else:
            chain[key][token] = 1
    else:
        chain[key] = {}
        chain[key][token] = 1
    return chain

def scale_chain(chain):
    table_len = {}
    for key in chain:
        table_len[key] = 0
        for token in chain[key]:
            count = chain[key][token]
            weighted = int(count ** 1.3)
            chain[key][token] = weighted
            table_len[key] += weighted
    chain['table_len'] = table_len
    return chain

def select_link(chain, key):
    if key not in chain['table_len']: return False
    length = chain['table_len'][key]
    idx = random.randint(0, length-1)
    tokens = list(chain[key].keys())
    acc = 0
    for i in range(len(tokens)):
        token = tokens[i]
        acc += chain[key][token]
        if acc > idx:
            return token
    return False

def generate_firstname():
    names = [
        'Alaron', 'Aldrek', 'Ardo',
        'Barazak', 'Balur', 'Bombur', 'Bofur', 'Bnar',
        'Chakrir', 
        'Dendirsyr', 'Dorn',
        'Erwid',
        'Farsben', 'Fili', 'Fordreth',
        'Gadaric', 'Gimli', 'Graflyn', 'Gunder', 'Goltan', 'Grimn',
        'Haldrik', 'Heimoc', 'Helsbid', 'Helwright', 'Hoskuld',
        'Kalhor', 'Karsten', 'Kenth', 'Kili', 'Kulderik',
        'Lornir', 
        'Maarik', 'Meli',
        'Nomir',
        'Thorin',
        'Valamar', 'Valdan',
    ]
    return generate_name(names)

def generate_lastname():
    # Dwarven lastnames are often two-parters
    prenouns = [
        'strong', 'steady', 'barren',
        'mountain','hill','cliff','range','mine','crag','storm','root',
        'sword', 'spear', 'axe', 'hammer',
        'shaft', 'haft',
        'wolf', 'bear', 'tiger', 'rat',
        'eagle','raven','hawk','hen',
        'brown', 'gray', 'green', 'black', 'red',
        'coal', 'shale', 'iron', 'oak', 'steel', 'gravel',
        'wooden','oaken','ivy',
        'fire','earth','air','water'
    ]
    postnouns = [
        'mountain','hill','cliff','range','mine','crag','storm','root',
        'sword', 'spear', 'axe', 'hammer',
        'hand','tongue', 'skull',
        'talon','claw','beak','hawk',
        'borne', 'heim',
        'pants','vest','tunic','shirt',
    ]
    verbs = [
        'breaker','smiter','hewer','slasher','stealer'
    ]
    if random.randint(0,1) == 0:
        part1 = prenouns[random.randint(0, len(prenouns)-1)].capitalize()
        part2 = postnouns[random.randint(0, len(postnouns)-1)]
        return f"{part1}{part2}"
    else:
        part1 = prenouns[random.randint(0, len(prenouns)-1)].capitalize()
        part2 = verbs[random.randint(0, len(verbs)-1)]
        return f"{part1}{part2}"

for _ in range(50):
    print(f"{generate_firstname()} {generate_lastname()}")
