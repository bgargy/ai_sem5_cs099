class UnificationError(Exception):
    pass

def is_variable(x):
    return isinstance(x, str) and x.islower()

def occurs_check(var, expr, subst):
    if var == expr:
        return True
    elif is_variable(expr) and expr in subst:
        return occurs_check(var, subst[expr], subst)
    elif isinstance(expr, tuple):
        return any(occurs_check(var, sub_expr, subst) for sub_expr in expr)
    return False

def unify(expr1, expr2, subst=None):
    if subst is None:
        subst = {}

    if expr1 == expr2:
        return subst

    if is_variable(expr1):
        return unify_var(expr1, expr2, subst)

    if is_variable(expr2):
        return unify_var(expr2, expr1, subst)

    if isinstance(expr1, tuple) and isinstance(expr2, tuple):
        if len(expr1) != len(expr2):
            raise UnificationError("Arity mismatch: Cannot unify terms with different argument counts.")
        if expr1[0] != expr2[0]:
            raise UnificationError(f"Cannot unify terms with different function symbols: {expr1[0]} and {expr2[0]}")
        for sub_expr1, sub_expr2 in zip(expr1, expr2):
            subst = unify(sub_expr1, sub_expr2, subst)
        return subst

    raise UnificationError(f"Cannot unify {expr1} with {expr2}")

def unify_var(var, expr, subst):
    if var in subst:
        return unify(subst[var], expr, subst)
    elif is_variable(expr) and expr in subst:
        return unify(var, subst[expr], subst)
    elif occurs_check(var, expr, subst):
        raise UnificationError(f"Occurs check failed: {var} appears in {expr}")
    else:
        if var in subst and subst[var] != expr:
            raise UnificationError(f"Conflict in substitutions: {var} cannot be both {subst[var]} and {expr}")
        subst[var] = expr
        return subst

if __name__ == "__main__":
    try:
        expr1 = ('f', 'y', 'z')
        expr2 = ('f', 'p', 'x')
        substitution = unify(expr1, expr2)
        print("Unification successful. Substitution:", substitution)
    except UnificationError as e:
        print("Unification failed:", str(e))
