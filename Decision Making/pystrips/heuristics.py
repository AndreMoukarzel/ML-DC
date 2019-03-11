import util


def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''

    prepos = {}
    for prep in state:
        prepos[prep] = 0

    x = state
    for action in applicable(state, planning.actions):
        x.union(action.pos_effect)

        for effect in action.pos_effect:
            old_prepos = prepos

            sm = 0
            val = prepos.get(effect)
            if (val == None):
                sm = 1 + soma(prepos, action.precond)
            else:
                sm = min(1 + soma(prepos, action.precond), val)
            prepos[effect] = sm 

            if (old_prepos != prepos):
                break

        
    custo = 0    
    for key in prepos:
        custo += prepos.get(key)

    return custo


def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    prepos = {}
    for prep in state:
        prepos[prep] = 0

    x = state
    for action in applicable(state, planning.actions):
        x.union(action.pos_effect)

        for effect in action.pos_effect:
            old_prepos = prepos

            sm = 0
            val = prepos.get(effect)
            if (val == None):
                sm = 1 + soma(prepos, action.precond)
            else:
                sm = min(1 + soma(prepos, action.precond), val)
            prepos[effect] = sm 
        
            if (old_prepos != prepos):
                break

    maximo = 0  
    for key in prepos:
        maximo = max(maximo, prepos.get(key))

    return maximo


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    #pipi
    util.raiseNotDefined()
    ''' YOUR CODE HERE '''


def applicable(state, actions):
    appl = []

    for act in actions:
        valid = True

        inter = state.intersect(act.precond)
        for cond in act.precond:
            if cond not in inter:
                valid = False
                break

        if (valid):
            appl.append(act)

    return appl


def soma(dic, preconds):
    soma = 0

    for cond in preconds:
        val = dic.get(cond)
        if (val == None):
            return Integer.MAX_VALUE
        soma += val

    return soma