# The Rotom Programming language

<img src="https://images.wikidexcdn.net/mwuploads/wikidex/thumb/a/a5/latest/20160604220739/Rotom.png/240px-Rotom.png" alt="rotom pet" width="128"/>

> Yes, the pokemon

This is an in progress implementation of a js transpiled programming language, it aims to have a simply yet powerful syntax.

Example:

```
fn fact(x) -> 1 if x == 0 else x * fact(x - 1)

fn main() {
    let mut i = 0;
    let n = 5;
    while i < n {
        print "fact(" + i + "): " + fact(i);
        i = i + 1;
    }
}
```

JS transpilation:

```js
function fact(x) {
  return x === 0 ? 1 : x * fact(x - 1);
}

function main() {
  let i = 0;
  const n = 5;
  while (i < n) {
    console.log("fact(" + i + "): " + fact(i));
    i = i + 1;
  }
}

main();
```

Output:

```bash
1/2 Transpiling...
1/2 Transpilation succeded
2/2 Writing js file...
2/2 🥳 Finished!!!

fact(0): 1
fact(1): 1
fact(2): 2
fact(3): 6
fact(4): 24
```

## Examples

Check out [/examples/code](/examples/code) for more examples
