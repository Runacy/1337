import itertools

numbers='1337'
arithmetic='+-/*'
patterns = list(set(list(itertools.permutations(numbers, 4))))
operator_patterns = list(itertools.product(arithmetic, repeat=3))

def get_formulas(pattern: tuple, operators: tuple)->list:
    formula0=f"({pattern[0]}{operators[0]}{pattern[1]}){operators[1]}({pattern[2]}{operators[2]}{pattern[3]})"
    formula1=f"({pattern[0]}{operators[0]}{pattern[1]}){operators[1]}{pattern[2]}{operators[2]}{pattern[3]}"
    formula2=f"({pattern[0]}{operators[0]}{pattern[1]}{operators[1]}{pattern[2]}){operators[2]}{pattern[3]}"
    formula3=f"{pattern[0]}{operators[0]}({pattern[1]}{operators[1]}{pattern[2]}){operators[2]}{pattern[3]}"
    formula4=f"{pattern[0]}{operators[0]}({pattern[1]}{operators[1]}{pattern[2]}{operators[2]}{pattern[3]})"
    formula5=f"{pattern[0]}{operators[0]}{pattern[1]}{operators[1]}({pattern[2]}{operators[2]}{pattern[3]})"
    fomula6=f"{pattern[0]}{operators[0]}{pattern[1]}{operators[1]}{pattern[2]}{operators[2]}{pattern[3]}"
    return [formula0, formula1, formula2, formula3, formula4, formula5, fomula6]


def eval_through_error(formula)->float:
    try:
        return float(eval(formula))
    except ZeroDivisionError:
        return 0.0


def use_operators_sum(pattern: tuple, operators: tuple)->list:
    """
    pattern 数値の組み合わせ
    operators 四則演算の組み合わせ
    それぞれを組み合わせてevalで式評価を行う

    答えが 10.0の式のみを返す
    """
    return [formula for formula in get_formulas(pattern, operators) if eval_through_error(formula) == 10.0]


def check_operator_patterns(pattern: tuple) -> filter:
    """
    全パターン試して、計算式が含まれている配列のみを返す
    """
    map_object = map(lambda operators: use_operators_sum(pattern, operators), operator_patterns)
    return filter(lambda res: len(res)>0, map_object)

if __name__ == '__main__':
    result = map(check_operator_patterns, patterns)
    for filter_formula in result:
        for formula in filter_formula:
            print(f"式: {formula}")


