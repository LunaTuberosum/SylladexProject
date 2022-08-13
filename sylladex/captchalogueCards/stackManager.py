import pickle

class StackManager():
    stack = []

    def get_stack():
        return StackManager.stack

    def get_length():
        return len(StackManager.stack)

    def add_toStack(card):
        return StackManager.stack.append(card)

    def save_stack():
        with open("data/data.plk", "wb") as inStack:
            pickle.dump(StackManager.get_stack(), inStack, -1)

    def load_stack():
        with open("data/data.plk", "rb") as outStack:
            StackManager.stack = pickle.load(outStack)
            print(StackManager.get_stack())