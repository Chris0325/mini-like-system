# mini_like

1、use Redis as a backend.

2、use custom hash function to scale horizontally

## test

```
    # like actions
    mini_like.like(1, 1)
    mini_like.like(1, 2)
    mini_like.like(2, 3)
    mini_like.like(2, 1)

    # unlike actions
    mini_like.unlike(1, 1)
    mini_like.unlike(2, 3)
```

## test result

<img src="https://github.com/Chris0325/mini-like-system/blob/master/static/mini_like_test.png" width = "50%" />
