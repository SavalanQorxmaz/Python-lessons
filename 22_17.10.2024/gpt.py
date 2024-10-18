import string

n = int(input())
start = list(string.ascii_lowercase[:n])
max_len = 4 * n - 3

def main():
    patterns = []

    # Generate the top part of the pattern
    for i in range(n):
        alpha = start[:n-i][::-1] + start[1:n-i]  # Generate the current line's letter pattern
        pattern = "-".join(alpha).center(max_len, '-')  # Join the pattern with '-' and center it
        patterns.append(pattern)  # Store the pattern

    # Combine the top and bottom parts and print the final pattern
    full_pattern = patterns[::-1] + patterns[1:]  # Reverse and combine the pattern
    print("\n".join(full_pattern))  # Print each line

main()