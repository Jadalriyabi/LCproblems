# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true


def scoresClump(scores):
    # Iterate through the list, checking every group of 3 adjacent scores, this wis why we check len(scores) - 2
    for i in range(len(scores) - 2 ):
        # Check if the difference between the smallest and largest score is at most 2
        if scores[i+2] - scores[i] <= 2:
            return True

    return False