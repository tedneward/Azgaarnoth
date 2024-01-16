names = {
    'Aakheperkare',
    'Addaya',
    'Ahhotpe',
    'Ahmes',
    'Ahmose',
    'Ahmose-saneit',
    'Ahmose-sipari',
    'Akencheres',
    'Akunosh',
    'Amenakht',
    'Amenakhte',
    'Amenemhat',
    'Amenemheb',
    'Amenemopet',
    'Amenhirkopshef',
    'Amenhirwenemef',
    'Amenhotpe',
    'Amenmesse',
    'Amenmose',
    'Amennestawy',
    'Amenope',
    'Amenophis',
    'Amenwahsu',
    'Ameny',
    'Amosis-ankh',
    'Amoy',
    'Amunemhat',
    'Amunherpanesha',
    'Amunhotpe',
    'Anen',
    'Ankh-Psamtek',
    'Ankhef',
    'Ankhefenamun',
    'Ankhefenkhons',
    'Ankhefenmut',
    'Ankhsheshonq',
    'Ankhtify',
    'Ankhtyfy',
    'Ankhu',
    'Ankhuemhesut',
    'Any',
    'Apophis'
}

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

import random

def select_link(chain, key):
    length = chain['table_len'][key]
    if not length:
        return False
    idx = random.randint(0, length-1)
    tokens = list(chain[key].keys())
    acc = 0
    for i in range(len(tokens)):
        token = tokens[i]
        acc += chain[key][token]
        if acc > idx:
            return token
    return False

for _ in range(10):
    print(generate_name([
        'Alaron',
        'Aldrek',
        'Barazak',
        'Balur',
        'Bombur',
        'Bofur',
        'Bnar',
        'Chakrir',
        'Dendirsyr',
        'Dorn',
        'Erwid',
        'Farsben',
        'Fili',
        'Gadaric',
        'Graflyn',
        'Haldrik',
        'Heimoc',
        'Helsbid',
        'Helwright',
        'Kalhor',
        'Karsten',
        'Kenth',
        'Kili',
        'Kulderik',
        'Lornir',
        'Maarik',
        'Meli',
        'Nomir',
        'Valamar',
        'Valdan',
    ]))
