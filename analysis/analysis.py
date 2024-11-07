import numpy as np
from aStar.aStar_search import AStarSearch
from uniformsearch.uniform_cost_search import UniformCostSearch
from structure.structure import Structure
import time
from collections import defaultdict
import json
import pandas as pd
import matplotlib.pyplot as plt



def generate_puzzle(num_moves):
    #Generate a puzzle that requires num_moves to solve
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    current_state = goal_state.copy()
    moves_made = []

    for _ in range(num_moves):
        puzzle = Structure(current_state)
        valid_moves = puzzle.get_valid_moves()
        # Avoid undoing the last move
        if moves_made:
            opposite_moves = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
            last_move = moves_made[-1]
            if opposite_moves[last_move] in valid_moves:
                valid_moves.remove(opposite_moves[last_move])

        move = np.random.choice(valid_moves)
        moves_made.append(move)
        puzzle.move(move)
        current_state = list(puzzle.grid[0])

    return current_state


def run_analysis(difficulty_levels=[2, 4, 8, 12, 16]):
   # analysis on different searches
    results = defaultdict(list)

    for difficulty in difficulty_levels:
        print(f"\nTesting difficulty level {difficulty} moves...")

        # Generate 10 different puzzles for each difficulty level
        for test_num in range(10):
            start_state = generate_puzzle(difficulty)

            # Test each algorithm
            algorithms = {
                'UCS': lambda: UniformCostSearch(start_state),
                'A* (Missing Tiles)': lambda: AStarSearch(start_state, heuristic='missing'),
                'A* (Euclidean)': lambda: AStarSearch(start_state, heuristic='euclidean')
            }

            for algo_name, algo_constructor in algorithms.items():
                # Running the search and measuring
                start_time = time.time()
                algo = algo_constructor()
                path = algo.search()
                end_time = time.time()

                if path is not None:
                    results['Algorithm'].append(algo_name)
                    results['Difficulty'].append(difficulty)
                    results['Test Number'].append(test_num + 1)
                    results['Nodes Expanded'].append(algo.expanded_nodes)
                    results['Time (s)'].append(end_time - start_time)
                    results['Solution Length'].append(len(path) if isinstance(path, list) else path)

    return pd.DataFrame(results)


def cleaning_data(data):
    #cleaning data
    # Average nodes expanded per difficulty level
    nodes_by_difficulty = data.groupby(['Algorithm', 'Difficulty'])['Nodes Expanded'].mean().reset_index()

    # Average time per difficulty level
    time_by_difficulty = data.groupby(['Algorithm', 'Difficulty'])['Time (s)'].mean().reset_index()

    # Convert to format needed
    def create_chart_data(df, value_column):
        chart_data = []
        for diff in sorted(df['Difficulty'].unique()):
            data_point = {'difficulty': str(diff)}
            for algo in df['Algorithm'].unique():
                value = df[(df['Difficulty'] == diff) & (df['Algorithm'] == algo)][value_column].iloc[0]
                data_point[algo] = float(value)
            chart_data.append(data_point)
        return chart_data

    nodes_data = create_chart_data(nodes_by_difficulty, 'Nodes Expanded')
    time_data = create_chart_data(time_by_difficulty, 'Time (s)')

    return {
        'nodes': nodes_data,
        'time': time_data
    }


def generate_performance_report():
    # Run the analysis
    print("Running search algorithm analysis...")
    results = run_analysis()

    # Prepare data for visualization
    viz_data = cleaning_data(results)

    # Create summary statistics
    summary = results.groupby('Algorithm').agg({
        'Nodes Expanded': ['mean', 'std'],
        'Time (s)': ['mean', 'std'],
        'Solution Length': ['mean', 'std']
    }).round(2)

    # Save the visualization data to a JSON file
    with open('search_analysis_results.json', 'w') as f:
        json.dump(viz_data, f)

    return results, viz_data, summary


def plot_results(results):
    """Create performance comparison plots using Matplotlib"""
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Aggregate data by algorithm and difficulty
    grouped = results.groupby(['Difficulty', 'Algorithm'])
    nodes_data = grouped['Nodes Expanded'].mean().unstack()
    time_data = grouped['Time (s)'].mean().unstack()

    # Plot nodes expanded
    nodes_data.plot(kind='bar', ax=ax1)
    ax1.set_title('Nodes Expanded vs. Problem Difficulty')
    ax1.set_xlabel('Problem Difficulty (Number of Moves)')
    ax1.set_ylabel('Average Nodes Expanded')
    ax1.legend(title='Algorithm')

    # Plot time taken
    time_data.plot(kind='bar', ax=ax2)
    ax2.set_title('Search Time vs. Problem Difficulty')
    ax2.set_xlabel('Problem Difficulty (Number of Moves)')
    ax2.set_ylabel('Average Time (seconds)')
    ax2.legend(title='Algorithm')

    plt.tight_layout()
    plt.savefig('search_comparison.png')
    print("\nPlots have been saved as 'search_comparison.png'")
    plt.close()


def generate_performance_report():
    """Generate a complete performance report"""
    results = run_analysis()

    # Create summary statistics
    summary = results.groupby('Algorithm').agg({
        'Nodes Expanded': ['mean', 'std'],
        'Time (s)': ['mean', 'std'],
        'Solution Length': ['mean', 'std']
    }).round(2)

    print("\nSummary Statistics:")
    print(summary)

    # Generate plots
    plot_results(results)

    return results, summary

if __name__ == "__main__":
    results, summary = generate_performance_report()
    print("\nSummary Statistics:")
    print(summary)
    print("\nVisualization data has been saved to 'search_analysis_results.json'")