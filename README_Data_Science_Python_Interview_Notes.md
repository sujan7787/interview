# Data Science Python Interview Notes

This file explains a few Python interview topics in simple words, with analogies and examples.

## Lambda Function

### Definition

A `lambda` function is a small function written in one line. It does not need a name.

Normal function:

```python
def multiply(x, y):
    return x * y
```

Same thing using lambda:

```python
a = lambda x, y: x * y
print(a(7, 19))
```

Output:

```text
133
```

### Layman Explanation

A lambda is like a quick shortcut function. You use it when the task is small and simple.

### Analogy

Think of a lambda function like a sticky note calculation.

Instead of writing a full recipe book for "multiply two numbers", you write one short instruction:

```text
take x and y, return x times y
```

### Explaining The Example Code

```python
a = lambda x, y: x * y
```

This means:

- `lambda` tells Python we are creating a small anonymous function.
- `x, y` are inputs.
- `x * y` is the result returned by the function.
- `a` stores that function so we can use it later.

```python
print(a(7, 19))
```

This means:

- Put `7` in place of `x`.
- Put `19` in place of `y`.
- Calculate `7 * 19`.
- Print the answer, which is `133`.

### Data Science Example

```python
df["price_with_tax"] = df["price"].apply(lambda x: x * 1.13)
```

This means:

- Take every value in the `price` column.
- Multiply it by `1.13`.
- Store the result in a new column called `price_with_tax`.

## range and xrange

### Definition

`range()` creates a sequence of numbers for looping.

In Python 3, `xrange()` does not exist. Python 3 `range()` already works efficiently like old Python 2 `xrange()`.

### Layman Explanation

Use `range()` when you want to repeat something a fixed number of times.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### Analogy

`range(5)` is like a ticket machine that gives numbers one by one: 0, 1, 2, 3, 4.

It does not need to print all tickets at once. It can give the next number when needed.

### Python 2 Difference

In Python 2:

- `range()` created a full list in memory.
- `xrange()` generated numbers one by one.

In Python 3:

- `range()` generates numbers efficiently.
- `xrange()` is removed.

### Interview Answer

Say this:

> In Python 3, there is no `xrange`. `range` behaves lazily and is memory efficient. In Python 2, `range` returned a list, while `xrange` generated values one by one.

## *args and **kwargs

### Definition

`*args` is used when a function can receive many positional arguments.

`**kwargs` is used when a function can receive many keyword arguments.

### Layman Explanation

Use `*args` when you do not know how many normal values will be passed.

Use `**kwargs` when you do not know how many named values will be passed.

### Analogy

`*args` is like a bag of unnamed items.

```text
apple, banana, mango
```

`**kwargs` is like labeled boxes.

```text
name = Anil
age = 25
city = Kathmandu
```

### Example: *args

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20, 30))
```

Output:

```text
60
```

Explanation:

- `*args` collects `10, 20, 30`.
- Python stores them like a tuple: `(10, 20, 30)`.
- `sum(args)` adds them.

### Example: **kwargs

```python
def show_student(**kwargs):
    print(kwargs)

show_student(name="Rita", age=22, course="Data Science")
```

Output:

```text
{'name': 'Rita', 'age': 22, 'course': 'Data Science'}
```

Explanation:

- `**kwargs` collects named values.
- Python stores them like a dictionary.

### Example: Both Together

```python
def interview_answer(topic, *points, **details):
    print("Topic:", topic)
    print("Points:", points)
    print("Details:", details)

interview_answer(
    "Python",
    "easy syntax",
    "many libraries",
    level="beginner",
    use="data science"
)
```

`topic` receives `"Python"`.

`*points` receives:

```python
("easy syntax", "many libraries")
```

`**details` receives:

```python
{"level": "beginner", "use": "data science"}
```

## Local and Global Variables

### Definition

A local variable is created inside a function and usually works only inside that function.

A global variable is created outside functions and can be accessed in many places in the file.

### Layman Explanation

Local means private to one function.

Global means available more widely.

### Analogy

A local variable is like money in your own pocket. Only you can use it.

A global variable is like money kept on the family table. Many people can see or use it.

### Local Variable Example

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Here, `message` is local because it is created inside `greet()`.

This will not work:

```python
def greet():
    message = "Hello"

print(message)
```

Why? Because `message` exists only inside the function.

### Global Variable Example

```python
name = "Sita"

def greet():
    print("Hello", name)

greet()
```

Here, `name` is global because it is created outside the function.

### Changing A Global Variable

```python
count = 0

def increase():
    global count
    count = count + 1

increase()
print(count)
```

Output:

```text
1
```

The `global count` line tells Python:

> I want to change the global `count`, not create a new local one.

### Interview Tip

Avoid changing global variables too much. It can make code confusing because many functions may change the same value.

In data science projects, prefer passing data into functions and returning results.

Better style:

```python
def add_tax(price):
    return price * 1.13

new_price = add_tax(100)
```

## Quick Memory Table

| Topic | Simple Meaning | Analogy |
|---|---|---|
| `lambda` | Small one-line function | Sticky note calculation |
| `range()` | Generates numbers for loops | Ticket machine |
| `xrange()` | Old Python 2 lazy range | Removed in Python 3 |
| `*args` | Many unnamed inputs | Bag of items |
| `**kwargs` | Many named inputs | Labeled boxes |
| Local variable | Works inside one function | Money in your pocket |
| Global variable | Available outside functions | Money on family table |

