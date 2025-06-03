import custom_logging

# Настройка логирования
class FileHandler:
    pass


class StreamHandler:
    pass


custom_logging.basicConfig(
    level=custom_logging.DEBUG,
    format="[%(levelname)s][%(asctime)s][%(name)s] %(message)s",
    handlers=[
        custom_logging.FileHandler("debug.log", mode="w"),
        custom_logging.StreamHandler()
    ]
)

logger = custom_logging.getLogger("TestLogger")

# Пример использования
logger.info("Информация для консоли")
logger.debug("Детальная информация для файла")


def getLogger(param):
    return None


def basicConfig(level, format, handlers):
    return None


def DEBUG():
    return None