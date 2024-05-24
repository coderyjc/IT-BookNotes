import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    # 洗牌
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, position, value):
        self._cards[position] = value
    # 继承MutableSequence的类必须实现__delitem__方法，这是MutableSequence类的一个抽象方法。
    def __delitem__(self, position):
        del self._cards[position]
    # 要实现insert方法，这是MutableSequence类的第三个抽象方法。
    def insert(self, position, value):
        self._cards.insert(position, value)