class MinStack:

    def __init__(self):
        self._stack: list[int] = []
        self._min = 0

    def push(self, val: int) -> None:
        # redefine _min
        if len(self._stack) == 0:
            self._min = val
        else:
            if val < self._min:
                self._min = val

        # append the value
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()

        # redefine _min
        if len(self._stack) > 0:
            self._min = min(self._stack)
        else:
            self._min = 0

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min
