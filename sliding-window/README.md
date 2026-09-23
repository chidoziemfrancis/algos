# Sliding Window

Used for problems involving a **contiguous** part of an array/string.

## Core Idea

Don't recalculate the whole window.

```text
new window = old window
            - element leaving
            + element entering
```

This can turn **O(n × k)** into **O(n)**.

## Fixed Window

Use when the window size is given (`k`).

```python
window = sum(nums[:k])
answer = window

for right in range(k, len(nums)):
    window += nums[right]
    window -= nums[right - k]
    answer = max(answer, window)
```

Think:

**ADD → REMOVE → UPDATE**

## Variable Window

Use when the window grows/shrinks based on a condition.

```python
left = 0

for right in range(len(nums)):
    # add nums[right]

    while window_is_invalid:
        # remove nums[left]
        left += 1

    # update answer
```

Think:

**RIGHT → expand**
**LEFT → shrink**

## How to Recognize It

Look for:

* subarray
* substring
* contiguous
* consecutive
* longest/shortest section

Ask:

> **Can I maintain information about the current window instead of recalculating it?**

## Why It Works

Sliding Window doesn't skip possible windows.

For `k = 3`:

```text
[2,1,5]
[1,5,1]
[5,1,3]
[1,3,2]
```

It checks every possible window, but calculates each one efficiently.

## Remember

> **Sliding Window = keep a contiguous window, move it, and update only what changed.**
