from abc import abstractmethod


class BitmovinApiLoggerBase(object):
    @abstractmethod
    def log(self, message, data=None):
        # type: (str, object) -> None
        pass

    @abstractmethod
    def error(self, message, data=None):
        # type: (str, object) -> None
        pass
