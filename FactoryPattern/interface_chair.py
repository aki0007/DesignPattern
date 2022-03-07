from abc import ABCMeta


class IChair(metaclass=ABCMeta):
    @staticmethod
    def get_dimensions():
        """Chair Interface"""
