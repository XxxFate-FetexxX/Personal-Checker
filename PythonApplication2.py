import sys

granted_access = False


def main() -> int:

    def granted_access(height: int, weight: int, name: str, age: int) -> bool:
        output = f"""Вход разрешен!
            Ваше имя: {name}.
            Ваш рост: {height} см.
            Ваш вес: {weight} кг.
            Ваш возраст: {age} лет.
        """

        print(output)
        return 0

    def not_access(factor: str) -> bool:
        print(f'Вход запрещен {factor}', flush=sys.stderr)
        return 1

    name = input('как вас зовут? ')

    height = input('Какой у вас рост? ')
    number_height = int(height)
    valid_height = 160 <= number_height and number_height <= 200 # False or True

    if not valid_height: # Если False
        return not_access('по росту')

    weight = input('Какой у вас вес? ')
    number_weight = int(weight)

    valid_weight = 40 <= number_weight and number_weight <= 80

    if not valid_weight:
        return not_access('по весу')

    age = input('Сколько вам лет? ')
    valid_age = int(age) >=18

    if not valid_age:
        return not_access('по возрасту')

    return granted_access(height, weight, name, age)

if __name__ == '__main__':
    res = main()

    if type(res) == int:
        exit(res)
    else:
        print('Что-то пошло не так 🤗')
