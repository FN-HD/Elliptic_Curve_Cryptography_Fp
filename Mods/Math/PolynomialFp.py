from Mods.Math.Fp_Element import FpElement


class Polynomial:
    # terms is an arg for inputting dict.
    def __init__(self, terms):
        # term['1'] is a coefficient of integer term.
        dict_ = {'1': FpElement(0)}

        for key in terms.keys():
            # We check this kwargs.
            if isinstance(terms[key], FpElement):
                terms[key] = FpElement(terms[key])
            else:
                raise TypeError('you should input int after =, for example x_2=7')

            if terms[key] == 0:
                continue

            t_key = Polynomial.normalize_representation_of(key)

            # input coefficient into terms.
            try:
                dict_[t_key] = terms[key] + dict_[t_key]
            except KeyError:
                dict_[t_key] = terms[key]

        self.terms = {}

        # we change the order of terms
        for key in Polynomial.sort_order_of(list(dict_.keys())):
            self.terms[key] = dict_[key]

    def get_differential_f(self, var):
        if self.has(var):
            term = {}

            for v in self.vars:
                t_var = []
                t_index = 0
                having_var = False

                for u in v.split('*'):
                    if u.split('^')[0] == var:
                        t_index = int(u.split('^')[1])
                        t_var.append(var+'^'+str(t_index - 1))
                        having_var = True
                    else:
                        t_var.append(u)

                if not having_var:
                    continue

                s = '*'.join(t_var)

                term[s] = self.terms[v] * t_index

            return Polynomial(term)
        else:
            raise TypeError('This Polynomial does not have the var you input')

    def has(self, var):
        return var in self.type_of_var

    def input(self, value, var):
        if self.has(var):
            term = {}

            for v in self.vars:
                t_var = []
                t_index = 0

                for u in v.split('*'):
                    if u.split('^')[0] == var:
                        t_index = int(u.split('^')[1])
                    else:
                        t_var.append(u)

                if len(t_var) == 0:
                    t_var = ['1']

                s = '*'.join(t_var)

                try:
                    term[s] = self.terms[v] * (value**t_index) + term[s]
                except KeyError:
                    term[s] = self.terms[v] * (value**t_index)

            return Polynomial(term)
        else:
            raise TypeError('This Polynomial does not have the var you input')

    def __add__(self, other):
        if isinstance(other, Polynomial):
            s_vars = self.vars
            o_vars = other.vars
            terms = {}

            for var in list(set(s_vars + o_vars)):
                term = 0
                if var in s_vars:
                    term += self[var]
                if var in o_vars:
                    term += other[var]
                terms[var] = term

            return Polynomial(terms)
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.terms == other.terms

    def __getattr__(self, item):
        if item == 'vars':
            # We can get the list of strings,
            # which is (variables of the polynomial)_(index of the variebles).
            return list(self.terms.keys())
        elif item == 'cofs':
            # we can get the list of the coefficients of the polynomial
            return list(self.terms.values())
        elif item == 'items':
            # We can get the list of equation item,
            # which is a tuple (var,cof).
            return list(self.terms.items())
        elif item == 'type_of_var':
            vars_list = []

            for var in self.vars:
                if var == '1':
                    continue
                for v in var.split('*'):
                    if not v.split('^')[0] in vars_list:
                        vars_list.append(v.split('^')[0])

            return vars_list
        elif item == 'deg':
            # we can get degree of this polynomial.
            deg = 0
            for var in self.vars:
                var_split_list = var.split('_', 1)
                if len(var_split_list) == 2:
                    if deg < int(var_split_list[1]):
                        deg = int(var_split_list[1])

            return deg
        else:
            raise AttributeError(item)

    def __getitem__(self, item):
        if item in self.vars:
            # we can get the coefficient of the item.
            return self.terms[item]
        else:
            raise AttributeError(item)

    # we can get the number of the var items.
    def __len__(self):
        if self['1'] == 0:
            return len(self.terms) - 1
        else:
            return len(self.terms)

    def __neg__(self):
        return self * (-1)

    def __mul__(self, other):
        if isinstance(other, (int, FpElement, float)):
            terms = {}
            for var in self.vars:
                terms[var] = self[var] * other
            return Polynomial(terms)
        elif isinstance(other, Polynomial):
            terms = {}
            for var1 in self.vars:
                for var2 in other.vars:
                    terms[var1+'*'+var2] = self[var1] * other[var2]
            return Polynomial(terms)
        else:
            return NotImplemented

    def __iter__(self):
        return self.items.__iter__()

    def __reversed__(self):
        return reversed(self.items)

    def __rmul__(self, other):
        if isinstance(other, FpElement):
            return self * other
        else:
            return NotImplemented

    def __str__(self):
        # eq means the right-hand side, such as polynomial.
        eq = ''

        for var in self.vars:
            cof = self[var]

            # we add a sign of the var in string of the polynomial.
            if cof == FpElement(0):
                continue
            elif eq != '':
                eq += ' + '

            # we add integer term.
            if var == '1':
                eq += str(cof)
                continue

            # we edit term, whose cof is 1. (1*x -> x)
            if cof != FpElement(1):
                eq += str(cof)

            eq += var

        var_list = self.type_of_var

        if len(var_list) == 0:
            var_list = ['x']

        return 'f(' + ', '.join(var_list) + ') = ' + eq

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return self + (-other)
        else:
            return NotImplemented

    # The following methods are used in __init__
    # we can normalize representation of key of term
    @staticmethod
    def normalize_representation_of(key):
        splited_key_dic = {}

        for k in sorted(key.split('*')):
            value = k
            index = 1

            if '^' in k:
                value = k.split('^')[0]
                index = int(k.split('^')[1])
            elif k == '1':
                index = 0

            if index == 0:
                continue
            elif index < 0:
                raise TypeError('you input wrong. index='+str(index))

            if value in splited_key_dic.keys():
                splited_key_dic[value] = index + splited_key_dic[value]
            else:
                splited_key_dic[value] = index

        if splited_key_dic == {}:
            return '1'
        else:
            return '*'.join([k+'^'+str(splited_key_dic[k]) for k in splited_key_dic.keys()])

    # we can sort key of term.
    @staticmethod
    def sort_order_of(keys):
        k = 0

        while k < len(keys):
            i = k
            for j, key in enumerate(keys[k:]):
                if Polynomial.greater_in_key(key, keys[i]):
                    i = j + k

            t = keys[i]
            keys[i] = keys[k]
            keys[k] = t

            k = k + 1

        return keys

    # we can compare two key of term
    @staticmethod
    def greater_in_key(key1, key2):
        if key1 == '1':
            return False
        elif key2 == '1':
            return True

        key1_split_list = key1.split('*')
        key2_split_list = key2.split('*')

        k = 0

        while k < len(key1_split_list) and k < len(key2_split_list):
            t1 = key1_split_list[k].split('^')
            t2 = key2_split_list[k].split('^')

            if t1[0] < t2[0]:
                return True
            elif t1[0] > t2[0]:
                return False

            if int(t1[1]) > int(t2[1]):
                return True
            elif int(t1[1]) < int(t2[1]):
                return False

            k = k + 1

        return len(key1_split_list) > len(key2_split_list)
