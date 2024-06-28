import random

def generate_mixed_sequence(length):
    sequence = [random.randint(1, 10)]  # Start with a random number
    current_length = 1

    while current_length < length:
        pattern = random.choice(["AP", "GP", "trend"])
        segment_length = min(random.randint(2, 5), length - current_length)
        
        if pattern == "AP":
            common_diff = random.randint(-5, 5)
            for _ in range(segment_length):
                sequence.append(sequence[-1] + common_diff)
        elif pattern == "GP":
            common_ratio = random.uniform(0.5, 2)
            for _ in range(segment_length):
                sequence.append(int(sequence[-1] * common_ratio))
        else:  # trend
            trend = random.choice(["increasing", "decreasing", "fluctuating"])
            for _ in range(segment_length):
                if trend == "increasing":
                    sequence.append(sequence[-1] + random.randint(1, 5))
                elif trend == "decreasing":
                    sequence.append(sequence[-1] - random.randint(1, 5))
                else:
                    sequence.append(sequence[-1] + random.randint(-5, 5))
        
        current_length += segment_length

    return sequence[:length]  # Ensure we return exactly 'length' items

def main():
    sequence_length = int(input("Enter the number of items in the sequence: "))
    sequence = generate_mixed_sequence(sequence_length)
    
    print(f"Mixed sequence of length {sequence_length}:")
    print(sequence)

if __name__ == "__main__":
    main()