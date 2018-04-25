STARTING_SCHEMA = {
    'tasks': {
        'current': None,
        'queued': [],
        'completed': []
    },
    'vision': {
        'cubes': [],
        'obstacles': [],
        'robot': {
            'y': -1,
            'x': -1,
            'angle': 0
        },
        'path': {
            'actual': [],
            'currentPlan': [],
            'oldPlans': []
        }
    },
    'cubes': [],
    'obstacles': [],
    'robot': {
        'position': {
            'x': -1,
            'y': -1
        },
        'angle': 0
    },
    'time': {
        'start': 0,
        'stop': 0
    },
    'flag': {
        'visual': [],
        'name': '',
        'number': -1
    },
    'nextColour': 99,
}