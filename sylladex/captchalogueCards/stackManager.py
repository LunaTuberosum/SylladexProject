import pygame as pg
import pickle

class StackManager():
    stack = pg.sprite.LayeredUpdates()

    def get_stack():
        return StackManager.stack

    def get_length():
        return len(StackManager.stack)

    def get_top_card():
        for index, card in enumerate(StackManager.stack):
            if index == 0:
                return card

    def add_toStack(card):
        return StackManager.stack.add(card)

    def save_stack():
        with open("data/data.plk", "wb") as inStack:
            pickle.dump(StackManager.get_stack(), inStack, -1)

    def load_stack():
        with open("data/data.plk", "rb") as outStack:
            StackManager.stack = pickle.load(outStack)
            print(StackManager.get_stack())