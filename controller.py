import view
import model
import logger


def run_work(choose):
    if choose == 1:
        print(model.find(logger.get_base(), input('Введите запрос поиска  ')))
    elif choose == 2:
        logger.writer(input('Введите данные нового работника  '))

    elif choose == 3:
        base = model.delete(logger.get_base(), input('Введите данные работника для удаления    '))
        
        logger.rewriter(base)

    # elif choose == 4:


run_work(view.user_choose())
# run_work(1)
