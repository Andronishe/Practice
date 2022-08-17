from Channel import Chanel
from Picture import Picture


class BitPlaneExtractor:
    @staticmethod
    def __extract_bit(source, plane):
        return source & (1 << plane - 1)

    @staticmethod
    def extract(img: Picture, chanel: Chanel, plane):
        bytes_ = 0
        if chanel == Chanel.RED:
            bytes_ = img.get_red()
        elif chanel == Chanel.GREEN:
            bytes_ = img.get_green()
        elif chanel == Chanel.BLUE:
            bytes_ = img.get_blue()
        lst = [BitPlaneExtractor.__extract_bit(i, plane) for i in bytes_]
        return lst




