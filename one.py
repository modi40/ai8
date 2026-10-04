import math

class GameTreeEvaluator:
    def __init__(self, branching_factor=2, depth=3, leaf_values=None):
        self.branching_factor = branching_factor
        self.depth = depth
        self.leaf_values = leaf_values if leaf_values else [3, 5, 2, 9, 12, 5, 23, 23]
        self.minimax_nodes_visited = 0
        self.alphabeta_nodes_visited = 0
        self.pruned_count = 0

    def minimax(self, depth, node_index, is_max):
        self.minimax_nodes_visited += 1
        if depth == self.depth:
            return self.leaf_values[node_index]
            
        if is_max:
            best = -math.inf
            for i in range(self.branching_factor):
                val = self.minimax(depth + 1, node_index * self.branching_factor + i, False)
                best = max(best, val)
            return best
        else:
            best = math.inf
            for i in range(self.branching_factor):
                val = self.minimax(depth + 1, node_index * self.branching_factor + i, True)
                best = min(best, val)
            return best

    def alphabeta(self, depth, node_index, is_max, alpha, beta):
        self.alphabeta_nodes_visited += 1
        if depth == self.depth:
            return self.leaf_values[node_index]
            
        if is_max:
            best = -math.inf
            for i in range(self.branching_factor):
                val = self.alphabeta(depth + 1, node_index * self.branching_factor + i, False, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    remaining = self.branching_factor - 1 - i
                    self.pruned_count += remaining
                    break
            return best
        else:
            best = math.inf
            for i in range(self.branching_factor):
                val = self.alphabeta(depth + 1, node_index * self.branching_factor + i, True, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    remaining = self.branching_factor - 1 - i
                    self.pruned_count += remaining
                    break
            return best

def main():
    leaves = [10, 9, 14, 18, 5, 4, 50, 3]
    evaluator = GameTreeEvaluator(branching_factor=2, depth=3, leaf_values=leaves)
    
    print("Performance Comparison: Minimax vs Alpha-Beta Pruning")
    print("Leaf Node Values:", leaves)
    
    score_mm = evaluator.minimax(0, 0, True)
    score_ab = evaluator.alphabeta(0, 0, True, -math.inf, math.inf)
    
    print("-" * 50)
    print(f"Algorithm                  Minimax      Alpha-Beta")
    print(f"Optimal Root Value         {score_mm:<12} {score_ab}")
    print(f"Total Evaluated Nodes      {evaluator.minimax_nodes_visited:<12} {evaluator.alphabeta_nodes_visited}")
    print(f"Pruned Sub-branches        {0:<12} {evaluator.pruned_count}")
    savings = (1 - evaluator.alphabeta_nodes_visited / evaluator.minimax_nodes_visited) * 100
    print(f"Computational Savings      0.00%        {savings:.2f}%")
    print("-" * 50)

if __name__ == '__main__':
    main()
