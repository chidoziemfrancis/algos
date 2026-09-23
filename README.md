# Algos

My data structures and algorithms practice space. LeetCode solutions, topic notes I can revise from, and the checklist I follow before writing any code.

## Revision Notes

| Topic | Notes |
| ----- | ----- |
| Sliding Window | [sliding-window/README.md](sliding-window/README.md) |
| Two Pointers | [two-pointers/README.md](two-pointers/README.md) |
| Prefix Sum | [prefix-sum/](prefix-sum/) |
| OOP | [oop/README.md](oop/README.md) |
| Design Patterns | [design-patterns/](design-patterns/) |
| Linked List | [linked-list/](linked-list/) |
| Stack | [stack/](stack/) |
| Trees | [trees/](trees/) |
| Recursion | [recursion/](recursion/) |
| Searching | [searching/](searching/) |
| Sorting | [sorting/](sorting/) |
| Strings | [strings/](strings/) |
| Arrays | [array/](array/) |

---

# DSA Problem-Solving Checklist

**Don't code immediately. Understand the problem first.**

## 1. Identify the Input

What are we given?

```text
Array?
String?
Number?
Linked List?
Tree?
Graph?
```

Write down the actual input.

```python
nums = [2, 7, 11, 15]
```

## 2. Identify the Output

What exactly do we need to return?

```text
Number?
Boolean?
Array?
Index?
String?
```

## 3. Understand the Rules

What are we allowed or not allowed to do?

Look for important words like:

```text
different
before
after
sorted
contiguous
unique
at most
exactly
```

## 4. Explain It in Plain English

Rewrite the problem in your own words.

Ask:

> **What am I actually being asked to find?**

If you cannot explain it simply, don't code yet.

## 5. Look for a Pattern

Ask whether the problem suggests:

```text
Two Pointers
Sliding Window
Hash Map / Set
Stack
Binary Search
Recursion
Heap
Linked List
Tree
Graph
Dynamic Programming
```

Don't choose a pattern just because you've seen it before.

Ask **why it fits**.

## 6. What Do I Need to Remember?

Decide what information must be stored while solving.

Examples:

```text
min_price
max_profit
frequency_map
left
right
stack
```

Ask:

> **What information from the previous steps do I need for the next step?**

## 7. Walk Through the Example

Do it manually before coding.

Example:

```text
prices = [7, 1, 5, 3, 6, 4]
```

Track your variables:

```text
price = 7
min_price = min(7, 7) = 7
profit = 7 - 7 = 0
max_profit = 0
```

Then continue step by step.

## 8. Write the Code

Only after you understand the steps.

Start with the simplest code that follows your reasoning.

## 9. Test It

Test three kinds of input.

**Normal case**

```text
[7,1,5,3,6,4]
```

**Edge case**

```text
[7,6,4,3,1]
```

**Small case**

```text
[1,2]
```

Ask:

> **Does my code handle the important cases?**

## 10. Complexity

Always ask:

```text
Time: ?
Space: ?
```

Example:

```text
Time:  O(n)
Space: O(1)
```

## Quick Version

When you're stuck, remember:

```text
1. INPUT
2. OUTPUT
3. RULES
4. PLAIN ENGLISH
5. PATTERN
6. WHAT DO I NEED TO REMEMBER?
7. WALK THROUGH EXAMPLE
8. CODE
9. TEST
10. COMPLEXITY
```

> **Understand, Plan, Trace, Code, Test.**

**Never rush to the code.**

---

# LeetCode Solutions

Solutions are synced automatically by [LeetHub v2](https://github.com/arunbhardwaj/LeetHub-2.0). The topic index below is generated, so edit above this line only.

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0053-maximum-subarray](https://github.com/chidoziemfrancis/algos/tree/master/0053-maximum-subarray) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/chidoziemfrancis/algos/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Divide and Conquer
|  |
| ------- |
| [0053-maximum-subarray](https://github.com/chidoziemfrancis/algos/tree/master/0053-maximum-subarray) |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Dynamic Programming
|  |
| ------- |
| [0053-maximum-subarray](https://github.com/chidoziemfrancis/algos/tree/master/0053-maximum-subarray) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/chidoziemfrancis/algos/tree/master/0121-best-time-to-buy-and-sell-stock) |
## Hash Table
|  |
| ------- |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Sorting
|  |
| ------- |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Boyer–Moore Majority Vote Algorithm
|  |
| ------- |
| [0169-majority-element](https://github.com/chidoziemfrancis/algos/tree/master/0169-majority-element) |
## Heap (Priority Queue)
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/chidoziemfrancis/algos/tree/master/0347-top-k-frequent-elements) |
<!---LeetCode Topics End-->