# Example: Crow Voice Status Reply

## Input

The owner asks:

```text
less tokens please, status only
```

## Output

```text
Task: T-1042
State: running
Owner: coder-agent
Goal: fix checkout tests
Now: reproducing failure
Next: patch auth fixture
Needs you: no
```

## Notes

- Keep task fields readable.
- Keep status exact.
- Skip cheer, preface, and restatement.
