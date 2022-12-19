import view
import model
import logger


def run_work():
    choose = view.user_choose()
    if choose == 1:
        print('\n'.join(model.find(logger.get_base(), input('Введите запрос поиска  '))))
    elif choose == 2:
        logger.writer(input('Введите данные нового работника  '))
    elif choose == 3:
        base = model.delete(logger.get_base(), input(
            'Введите данные работника для удаления    '))
        logger.rewriter(base)
    elif choose == 4:
        worker = model.find(logger.get_base(), input(
            'Введите сотрудника для изменения  '))
        while len(worker) != 1:
            print(worker)
            worker = model.find(logger.get_base(), input(
                'Нашлось несколько работников! Конкретезируйте запрос  '))
        new_worker = model.change(worker)
        base = model.delete(logger.get_base(), new_worker[1])
        logger.rewriter(base)
        logger.writer(new_worker[0])
