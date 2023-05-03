import re

def predict_aggregator(text):
    # Define regular expressions to match each aggregator
    count_regex = re.compile(r'\b(how many|count|number of)\b', re.IGNORECASE)
    sum_regex = re.compile(r'\b(sum|total)\b', re.IGNORECASE)
    max_regex = re.compile(r'\b(max|highest)\b', re.IGNORECASE)
    min_regex = re.compile(r'\b(min|lowest)\b', re.IGNORECASE)
    
    # Match the regular expressions to the input text
    if count_regex.search(text):
        return "COUNT"
    elif sum_regex.search(text):
        return "SUM"
    elif max_regex.search(text):
        return "MAX"
    elif min_regex.search(text):
        return "MIN"
    else:
        return None

# Example usage
text = "who has the highest salary"
aggregator = predict_aggregator(text)
print(aggregator)  # Output: MAX
