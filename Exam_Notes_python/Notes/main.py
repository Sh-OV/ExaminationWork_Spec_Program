#import view as cr 
import logger as lg

logger = lg.get_logger(__name__)

def main():
    import view as vw
    logger.info("Программа стартует")
    vw.process(msg="сообщение")
    logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    logger.info("Программа завершила работу")

if __name__ == "__main__":
    main()