const initialState = {
    gameState: {
        'tasks': {
            'current': null,
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
    },
    configModalIsActive: false,
    serverConfiguration: {
        robot: {
            address: 'design-whitecat.local',
            port: 8080,
            connected: false
        },
        serverImage: {
            address: 'localhost',
            port: 5000,
            connected: false
        }
    },
};
export default initialState;
