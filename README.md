# The Rotom Programming language

<img src="https://images.wikidexcdn.net/mwuploads/wikidex/thumb/a/a5/latest/20160604220739/Rotom.png/240px-Rotom.png" alt="rotom pet" width="128"/>

> Made for fun

This is an in progress implementation of a js transpiled programming language, it aims to have a simply yet powerful syntax.

Example:

```
fn fact(x) -> 1 if x == 0 else x * fact(x - 1)

fn sayHi() -> "Hi"

fn printit(start, end, step, callback) {
    let mut i = start;
    let mut count = 0;

    while i < end {
        print callback();
        i = i + step;
        count = count + 1;
    }

    count
}

fn main() {
    print fact(5);
    let num = printit(0, 5, 1, sayHi);
    print "Ran: " + num + " times";
    nil
}
```

JS transpilation:

```js
function fact(x) {
  return x === 0 ? 1 : x * fact(x - 1);
}

function sayHi() {
  return "Hi";
}

function printit(start, end, step, callback) {
  let i = start;
  let count = 0;
  while (i < end) {
    console.log(callback());
    i = i + step;
    count = count + 1;
  }
  return count;
}

function main() {
  console.log(fact(5));
  const num = printit(0, 5, 1, sayHi);
  console.log("Ran: " + num + " times");
  return null;
}

main();
```

Output:

```
120
Hi
Hi
Hi
Hi
Hi
Ran: 5 times
```
