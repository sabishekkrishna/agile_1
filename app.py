

def sum_list(numbers):
    return sum(numbers)

def count_negatives(numbers):
    int count=0
    for i in numbers:
        if numbers[i]<0:
            count++ 
    return count


if __name__ == "__main__":
    sample = [3,2,5,-1,10,-4]
    print(f"Sum: {find_min(sample)}")
    print(f"Number of negatives: {count_odds(sample)}")
