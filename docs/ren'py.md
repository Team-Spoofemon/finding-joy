# Ren'Py
- [animation tools](https://www.youtube.com/watch?v=0VWV_610BPw)
- [screens](https://www.youtube.com/watch?v=R4Vvv_uapbk)

- enabling developer mode, enable shift + r and shift + d, shift + o for console???: https://www.renpy.org/doc/html/python.html#default-statement
    ```python
    # in options.rpy
    init python:
        config.developer = True
    ```

- `init:` allows you to declare variables earlier in the call stack, so they can be used in things like configs
    - example: declaring a dictionary `mapping` under `init:` in a file called `globals.rpy` will cause `mapping` to be available at all times, meaning full runtime global state manipulation
