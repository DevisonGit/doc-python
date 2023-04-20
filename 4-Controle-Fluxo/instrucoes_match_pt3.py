from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input('Enter your choice of red, blue or green: '))

match color:
    case Color.RED:
        print('i see red!')
    case Color.GREEN:
        print('grass is green')
    case Color.BLUE:
        print(f'im feeling the blues')
