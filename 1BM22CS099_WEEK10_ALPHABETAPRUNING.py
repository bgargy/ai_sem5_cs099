import sys

# Alpha-Beta Pruning Function
def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = -sys.maxsize
        for i in range(2):  # Two children per node
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                print(f"Pruning at Node-{node_index}, depth: {depth}, alpha: {alpha}, beta: {beta}")
                break
        return best
    else:
        best = sys.maxsize
        for i in range(2):  # Two children per node
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                print(f"Pruning at Node-{node_index}, depth: {depth}, alpha: {alpha}, beta: {beta}")
                break
        return best

# Function to take user input for leaf node values
def get_user_input():
    print("Enter the leaf node values (space-separated): ")
    leaf_values = list(map(int, input().split()))

    # Validate that leaf nodes form a complete binary tree
    n = len(leaf_values)
    if n & (n - 1) != 0:  # Check if n is a power of 2
        print("Error: Number of leaf nodes must be a power of 2 for a complete binary tree.")
        return get_user_input()
    return leaf_values

# Calculate the tree depth from the number of leaf nodes
def calculate_tree_depth(leaf_count):
    depth = 0
    while leaf_count > 1:
        leaf_count //= 2
        depth += 1
    return depth

# Main Function
def main():
    # Get user input for leaf nodes
    leaf_values = get_user_input()
    max_depth = calculate_tree_depth(len(leaf_values))

    # Perform Alpha-Beta Pruning
    print("\nStarting Alpha-Beta Pruning...")
    root_value = alpha_beta_pruning(0, 0, True, leaf_values, -sys.maxsize, sys.maxsize, max_depth)
    print(f"\nOptimal Value at Root: {root_value}")

# Run the Program
if __name__ == "__main__":
    main()
import sys

# Alpha-Beta Pruning Function
def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = -sys.maxsize
        for i in range(2):  # Two children per node
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                print(f"Pruning at Node-{node_index}, depth: {depth}, alpha: {alpha}, beta: {beta}")
                break
        return best
    else:
        best = sys.maxsize
        for i in range(2):  # Two children per node
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                print(f"Pruning at Node-{node_index}, depth: {depth}, alpha: {alpha}, beta: {beta}")
                break
        return best

# Function to take user input for leaf node values
def get_user_input():
    print("Enter the leaf node values (space-separated): ")
    leaf_values = list(map(int, input().split()))

    # Validate that leaf nodes form a complete binary tree
    n = len(leaf_values)
    if n & (n - 1) != 0:  # Check if n is a power of 2
        print("Error: Number of leaf nodes must be a power of 2 for a complete binary tree.")
        return get_user_input()
    return leaf_values

# Calculate the tree depth from the number of leaf nodes
def calculate_tree_depth(leaf_count):
    depth = 0
    while leaf_count > 1:
        leaf_count //= 2
        depth += 1
    return depth

# Main Function
def main():
    # Get user input for leaf nodes
    leaf_values = get_user_input()
    max_depth = calculate_tree_depth(len(leaf_values))

    # Perform Alpha-Beta Pruning
    print("\nStarting Alpha-Beta Pruning...")
    root_value = alpha_beta_pruning(0, 0, True, leaf_values, -sys.maxsize, sys.maxsize, max_depth)
    print(f"\nOptimal Value at Root: {root_value}")

# Run the Program
if __name__ == "__main__":
    main()