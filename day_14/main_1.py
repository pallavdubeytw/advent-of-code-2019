from copy import deepcopy

pz_inp_txt = '''10 KVPH => 5 HPRK
5 RSTBJ => 5 QKBQL
2 GZWFN, 21 WBPFQ => 5 KMFWH
5 JDJB, 1 FSWFT, 1 NKVSV => 6 MGKSL
5 BCRHK => 9 KXFTL
23 NKVSV, 2 RSTBJ => 9 QPBVD
19 BKFVS, 7 JZBFT => 7 XWTQ
14 JLXP, 4 LSCL => 8 FWLTD
173 ORE => 5 TZSDV
2 FPVH, 1 JDJB, 3 KHRW => 2 QLNJ
1 HTGMX, 1 GVJVK, 2 RLRK => 2 HWBM
1 GLVHT, 1 PBCT, 5 ZWKGV, 1 QSVJ, 2 FWLTD, 3 CNVPB, 1 QGNL => 8 RNLTX
1 KXZTS => 2 BKFVS
1 KVPH, 6 PVHPV, 2 TZSDV => 4 RLRK
118 ORE => 1 VRVZ
7 MGKSL, 4 HWBM => 2 GZWFN
5 PVHPV => 7 HTGMX
25 LSCL, 12 GVMFW => 6 ZWKGV
1 CTPND, 1 KXZTS => 3 FRQH
1 KXFTL => 3 PBCT
1 CMPX => 4 KZNBL
2 HDQVB, 1 QPBVD => 5 CTPND
14 KVPH => 1 FCBQN
3 XWTQ, 22 CTHM, 4 KVPH, 4 BZTV, 1 KMFWH, 12 NRFK => 7 CXVR
1 GVJVK => 7 RSTBJ
1 GVJVK => 4 NSQHW
3 NKVSV => 8 KHRW
8 HDQVB, 9 BCRHK => 6 GVMFW
142 ORE => 7 KVPH
4 TZSDV => 2 GVJVK
4 KVPH, 10 HWBM => 3 NRFK
47 PBCT, 15 CXVR, 45 GVJVK, 23 KZNBL, 1 WFPNP, 14 RNLTX => 1 FUEL
1 PCBNG => 4 QLJXM
1 SHTQF => 2 FNWBZ
2 FCBQN, 1 BCRHK => 5 HVFBV
1 BZTQ => 9 CTHM
16 SHTQF => 3 BZTQ
11 PBCT, 5 PCBNG, 2 CTPND => 1 WBPFQ
3 KHRW => 4 FSWFT
12 HDQVB, 1 PBCT, 9 NRFK => 9 VLWJL
5 SHTQF, 8 HVFBV => 6 BZTV
2 KZNBL, 7 NRFK => 3 DVFS
18 HTLSF, 14 DVFS => 6 TLFNL
1 RSTBJ => 1 NKVSV
2 QLNJ, 7 BZTQ => 6 PCBNG
1 HTLSF, 19 CMPX => 7 JDJB
6 KZNBL, 3 QSVJ => 8 SHTQF
3 HTLSF, 1 VRVZ => 6 CMPX
1 MGKSL, 15 CTPND => 6 STNPH
2 NKVSV, 7 JDJB => 4 KXZTS
3 KVPH => 4 QSVJ
1 HPRK, 9 PCBNG, 2 KXFTL => 9 CNVPB
27 GZWFN, 1 VLWJL, 15 LSCL => 3 GLVHT
162 ORE => 4 HTLSF
193 ORE => 8 PVHPV
9 TLFNL, 1 KHRW => 6 HDQVB
6 QLJXM, 4 FCBQN => 7 JLXP
3 HTLSF, 21 NSQHW, 18 GVJVK => 7 BCRHK
1 HTGMX, 20 CMPX, 6 RSTBJ => 6 FPVH
4 KXZTS, 7 CNVPB, 1 STNPH => 2 LSCL
3 KXZTS, 1 PCBNG => 3 JZBFT
22 WBPFQ, 22 FRQH, 1 QLNJ, 4 CTHM, 3 GVMFW, 1 KMFWH, 4 QKBQL => 4 WFPNP
3 QLJXM, 11 FNWBZ, 3 WBPFQ => 5 QGNL'''


def print_list(in_list):
    print(str.join('\n', map(str, in_list)))


class ChemIO:
    def __init__(self, name, quantity):
        self.quantity = int(quantity)
        self.name = name

    def __repr__(self):
        return f'{self.quantity} {self.name}'

    @staticmethod
    def init_from_str(inp):
        inp = str.strip(inp)
        s = inp.split()
        return ChemIO(s[1], s[0])


class InChem(ChemIO):
    pass


class OutChem(ChemIO):
    pass


class Reaction:
    def __init__(self, in_chems, out_chem):
        self.out_chem = out_chem
        self.in_chems = in_chems

    def __repr__(self):
        in_str = str.join(', ', map(str, self.in_chems))
        return in_str + ' => ' + str(self.out_chem)

    def multiply(self, multiplyier):
        for in_chem in self.in_chems:
            in_chem.quantity *= multiplyier

        self.out_chem.quantity *= multiplyier

    @staticmethod
    def init_from_str(inp):
        inp = str.strip(inp)
        sp = inp.split('=>')

        in_chems_str = sp[0]
        in_chem_split = in_chems_str.split(',')

        in_chems = []
        for chem in in_chem_split:
            in_chems.append(InChem.init_from_str(chem))

        out_chem_str = sp[1]
        out_chem = OutChem.init_from_str(out_chem_str)

        return Reaction(in_chems, out_chem)


original_reactions = list(map(Reaction.init_from_str, pz_inp_txt.split('\n')))


def get_required_unit_for_each_chem(reactions):
    chem_units = {}
    for r in reactions:
        for in_chem in r.in_chems:
            if in_chem.name in chem_units:
                chem_units[in_chem.name] += in_chem.quantity
            else:
                chem_units[in_chem.name] = in_chem.quantity
    return chem_units


def get_produced_units_for_each_chem(reactions):
    chem_units = {}
    for r in reactions:
        if r.out_chem.name in chem_units:
            chem_units[r.out_chem.name] += r.out_chem.quantity
        else:
            chem_units[r.out_chem.name] = r.out_chem.quantity
    return chem_units


def find_extra_units_required(out_chem_units, in_chem_units):
    to_increase = []
    for chem in out_chem_units:
        if chem != 'FUEL':
            if out_chem_units[chem] < in_chem_units[chem]:
                to_increase.append(chem)
    return to_increase


def get_multiplier_with_respect_to_original_reaction(reactions, out_chem, units_to_produce):
    production_reaction = list(filter(lambda r: r.out_chem.name == out_chem, reactions))
    count = 2
    while True:
        if production_reaction[0].out_chem.quantity * count >= units_to_produce:
            reaction_multiplier[out_chem] = count
            break
        else:
            count += 1
    return count


reactions_copy = deepcopy(original_reactions)
in_chem_units = get_required_unit_for_each_chem(original_reactions)
out_chem_units = get_produced_units_for_each_chem(original_reactions)
extra_chem_units = find_extra_units_required(out_chem_units, in_chem_units)

while len(extra_chem_units) > 0:

    reaction_multiplier = {}
    for chem in extra_chem_units:
        reaction_multiplier[chem] = \
            get_multiplier_with_respect_to_original_reaction(original_reactions, chem, in_chem_units[chem])

    for chem in reaction_multiplier:
        original_production_reaction = list(filter(lambda r: r.out_chem.name == chem, original_reactions))
        tmp = deepcopy(original_production_reaction)
        tmp[0].multiply(reaction_multiplier[chem])

        modified_production_reaction = list(filter(lambda r: r.out_chem.name == chem, reactions_copy))
        modified_production_reaction[0].in_chems = tmp[0].in_chems
        modified_production_reaction[0].out_chem = tmp[0].out_chem

    in_chem_units = get_required_unit_for_each_chem(reactions_copy)
    out_chem_units = get_produced_units_for_each_chem(reactions_copy)
    extra_chem_units = find_extra_units_required(out_chem_units, in_chem_units)

in_chem_units = get_required_unit_for_each_chem(reactions_copy)

print(f'part 1: {in_chem_units["ORE"]}')


