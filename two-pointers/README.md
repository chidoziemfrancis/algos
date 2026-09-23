# Two Pointers

Two Pointers is used when we can solve a problem by keeping track of **two positions** in an array/string.

Instead of checking every possible pair:

```text
left →        ← right
[1, 2, 3, 4, 5, 6]
```

Move one or both pointers based on what we need.

This can often turn **O(n²) → O(n)**.

---

## Basic Template

```python
left = 0
right = len(nums) - 1

while left < right:

    # use nums[left] and nums[right]

    if condition:
        left += 1
    else:
        right -= 1
```

---

## Most Common: Sorted Array

Example: **Two Sum II**

Find two numbers that add up to `target`.

```python
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]

        if total < target:
            left += 1
        else:
            right -= 1

    return []
```

Why?

```text
sum too small → move LEFT right
sum too big   → move RIGHT left
```

This works because the array is **sorted**.

---

## Opposite Directions

```text
left →             ← right
[1, 2, 3, 4, 5, 6]
```

Common for:

* Two Sum II
* 3Sum
* Container With Most Water
* Valid Palindrome
* Trapping Rain Water

---

## Same Direction

Sometimes both pointers move from left → right.

```text
slow →
fast   →
[1, 2, 3, 4, 5, 6]
```

Example: removing duplicates.

```python
slow = 0

for fast in range(1, len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
```

Think:

```text
fast → explores
slow → builds the answer
```

---

## Two Pointers vs Sliding Window

**Two Pointers**

```text
left →       ← right
```

Two positions are used to solve the problem.

**Sliding Window**

```text
left → [ window ] → right
```

The two pointers specifically represent the **boundaries of a contiguous window**.

So:

> **Sliding Window is often a special use of two pointers.**

---

## How to Recognize Two Pointers

Look for:

* sorted array
* pairs
* two values
* palindrome
* opposite ends
* remove duplicates
* comparing elements from both sides

Ask:

> **Can I use two positions instead of checking every pair?**

---

## Remember

> **Two Pointers = use two indexes and move them intelligently instead of checking every possibility.**
