import util
from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    if solution is None:
        return True

    current_state = State().union(problem.init)
    for action in solution:
        if (not applicable(current_state, action) ):
            print("Action not applicable")
            return False

        old_state = current_state
        current_state = successor(current_state, action)
        next_state_check(old_state, current_state, action)

    if ( not is_goal(current_state, problem.goal) ):
        print("Result is not goal")
        return False

    return True


# Returns if action is applicable in current state
def applicable(state, action):
    applic = True

    inter = state.intersect(action.precond)
    for cond in action.precond:
        if cond not in inter:
            applic = False
            break

    return applic


def next_state_check(oldstate, newstate, action):
    common = oldstate.intersect(newstate)
    inter = newstate.intersect(action.pos_effect)
    for effect in action.pos_effect:
        if effect not in inter:
            return False
        if effect in common:
            return False

    inter = newstate.intersect(action.neg_effect)
    for effect in action.neg_effect:
        if effect in inter:
            return False
        if effect in common:
            return False


def successor(state, action):
    newstate = state.union(action.pos_effect)
    newstate = newstate.difference(action.neg_effect)
    return newstate


def is_goal(state, goal):
    valid = True

    for cond in goal:
        if cond not in state:
            valid = False
            break

    return valid