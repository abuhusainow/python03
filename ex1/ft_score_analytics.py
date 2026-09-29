import sys


def score_list(scores: list[str]) -> list[int]:
    valid_list: list[int] = []
    for score in scores:
        try:
            valid_list.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    return valid_list

# #IndexError
# def ft_scores(sys_input: list[str]) -> None:

def ft_score_analytics(scores: list[str]) -> None:
    print("=== Player Score Analytics ===")
    valid_list: list[int] = score_list(sys.argv[1:])
    if len(valid_list) < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {valid_list}")
        print(f"Total players: {len(valid_list)}")
        print(f"Total score: {sum(valid_list)}")
        print(f"Average score: {sum(valid_list)/len(valid_list):.1f}")
        print(f"High score: {max(valid_list)}")
        print(f"Low score: {min(valid_list)}")
        print(f"Score range: {max(valid_list) - min(valid_list)}")


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
