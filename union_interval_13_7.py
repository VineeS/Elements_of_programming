from collections import namedtuple

# Define a namedtuple for intervals
Interval = namedtuple('Interval', ['start', 'end'])

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on their start values
    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    
    merged_intervals = [sorted_intervals[0]]

    for interval in sorted_intervals[1:]:
        current_interval = merged_intervals[-1]

        if interval.start <= current_interval.end:
            print("interval",interval,"CI",current_interval,"merged_intervals[-1]",merged_intervals)
            # Overlapping intervals, merge them
            merged_intervals[-1] = Interval(
                current_interval.start,
                max(current_interval.end, interval.end)
            )
        else:
            # Non-overlapping interval, add it to the result
            merged_intervals.append(interval)
            print("non-overlapping interval",merged_intervals)

    return merged_intervals

# Example usage:
intervals = [
    Interval(0, 3),
    Interval(1, 1),
    Interval(3, 4),
    Interval(2, 4),
    Interval(5, 7),
    Interval(7, 8),
    Interval(9, 11),
    Interval(8,11),
    Interval(12, 14),
    Interval(12, 16),
    Interval(13, 15),
    Interval(16, 17)

]

union_intervals = merge_intervals(intervals)
print(union_intervals)
