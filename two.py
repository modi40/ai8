class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

def backward_chaining(goal, rules, known_facts, call_depth=0):
    indent = "  " * call_depth
    print(f"{indent}Investigating Goal: '{goal}'")
    
    if goal in known_facts:
        print(f"{indent}-> '{goal}' is directly known as a FACT.")
        return True
        
    matching_rules = [r for r in rules if r.consequent == goal]
    if not matching_rules:
        print(f"{indent}-> No rules found with consequent '{goal}'. Failure.")
        return False
        
    for idx, rule in enumerate(matching_rules, 1):
        print(f"{indent}Trying Rule {idx}: IF {' AND '.join(rule.antecedents)} THEN '{rule.consequent}'")
        all_subgoals_met = True
        for sub in rule.antecedents:
            if not backward_chaining(sub, rules, known_facts, call_depth + 1):
                all_subgoals_met = False
                break
        if all_subgoals_met:
            print(f"{indent}-> Rule {idx} SUCCEEDED. Proved '{goal}'.")
            known_facts.add(goal)
            return True
            
    print(f"{indent}-> All rules to prove '{goal}' failed.")
    return False

def main():
    rules = [
        Rule(['croaks', 'eats_flies'], 'frog'),
        Rule(['chirps', 'sings'], 'canary'),
        Rule(['frog'], 'green'),
        Rule(['canary'], 'yellow')
    ]
    facts = {'croaks', 'eats_flies'}
    goal = 'green'
    
    print("Backward Chaining Inference Mechanism")
    print("Rules in Knowledge Base:")
    for r in rules:
        print(f"  IF {' AND '.join(r.antecedents)} THEN {r.consequent}")
    print("Known Initial Facts:", sorted(list(facts)))
    print(f"Target Hypothesis to Prove: '{goal}'")
    print("=" * 55)
    
    result = backward_chaining(goal, rules, facts)
    print("=" * 55)
    print(f"Result: Hypothesis '{goal}' is", "PROVEN TRUE" if result else "CANNOT BE PROVEN")

if __name__ == '__main__':
    main()
