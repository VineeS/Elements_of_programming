from collections import namedtuple

# Define an Event namedtuple with start and end attributes
Event = namedtuple("Event", ["start", "end"])


# Sample events
events = [
    Event(start=1, end=2),
    Event(start=3, end=4),
    Event(start=5, end=6),
    Event(start=7, end=8),
    Event(start=9, end=10),
]

# Sort the events by their start times
events.sort(key=lambda event: event.start)


# Initialize variables to keep track of the maximum concurrent events and the current count
max_concurrent_events = 0
current_count = 0

# Iterate through the sorted events
for event in events:
    # If the current event starts before the previous one ends, it overlaps


    if event.start < events[current_count].end:
        current_count+=1
        max_concurrent_events = max(max_concurrent_events, current_count)
    else:
        print(current_count)
        current_count-=1
print(max_concurrent_events)




    # if event.start < events[current_count].end:
    #     print("event.start",event.start,"events[current_count].end",events[current_count].end)
    #     current_count += 1
    # else:
    #     # Update the maximum concurrent events if needed and reset the count
    #     max_concurrent_events = max(max_concurrent_events, current_count)
    #     current_count = 1

# Update the maximum concurrent events one last time
max_concurrent_events = max(max_concurrent_events, current_count)

print("Maximum concurrent events:", max_concurrent_events)
