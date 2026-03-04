def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return len(numbers) / total

scores = [85, 92, 78, 90, 88]

print("Average:", average(score))