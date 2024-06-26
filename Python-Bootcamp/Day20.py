def find_runner_up_score(num_scores, scores):
    # Remove duplicates by converting to set
    unique_scores = list(set(scores))

    # Sort unique scores in descending order
    unique_scores.sort(reverse=True)

    # The runner-up score is the second element in sorted unique scores
    runner_up_score = unique_scores[1]

    return runner_up_score


# Example usage:
if __name__ == "__main__":
    # Define the number of scores and the list of scores
    num_scores = 5
    scores = [2, 3, 6, 6, 1]

    # Find the runner-up score
    runner_up_score = find_runner_up_score(num_scores, scores)

    # Print the runner-up score
    print(runner_up_score)

