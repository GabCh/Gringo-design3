const fakePath = (level) => {
    return [...Array(1280).keys()].map(i => {
        const point = {};
        point.x = i;
        point.y = 720 / 2 + level;
        return point;
    });
};

const testingState =  {
    gameState: {
        vision: {
            cubes: [
                {
                    y: 170,
                    x: 1251,
                    colour: 0
                },
                {
                    y: 372,
                    x: 1250,
                    colour: 1
                },
                {
                    y: 638,
                    x: 1082,
                    colour: 2
                },
                {
                    y: 508,
                    x: 1253,
                    colour: 3
                },
                {
                    y: 366,
                    x: 346,
                    colour: 4
                },
                {
                    y: 286,
                    x: 1004,
                    colour: 5
                },
                {
                    y: 500,
                    x: 200,
                    colour: 99
                }
            ],
            obstacles: [
                {
                    y: 484,
                    x: 576
                },
                {
                    y: 274,
                    x: 1114
                }
            ],
            robot: {
                y: 60,
                x: 60,
                angle: 180
            },
            path: {
                currentPlan: fakePath(-200),
                actual: fakePath(0),
                oldPlans: [fakePath(180), fakePath(190), fakePath(200)]
            }
        },
        obstacles: [
            {
                position: {
                    x: 1.1529939603106125,
                    y: 0.9688352027610008
                }
            },
            {
                position: {
                    x: 2.229922346850733,
                    y: 0.5484728213977567
                }
            }
        ],
        cubes: [
            {
                position: {
                    x: 2.5041587575496114,
                    y: 0.3402933563416738
                },
                colour: 0
            },
            {
                position: {
                    x: 2.5021570319240722,
                    y: 0.7446419327006039
                },
                colour: 1
            },
            {
                position: {
                    x: 2.165867126833477,
                    y: 1.2771009490940464
                },
                colour: 2
            },
            {
                position: {
                    x: 2.50816220880069,
                    y: 1.016876617773943
                },
                colour: 3
            },
            {
                position: {
                    x: 0.6925970664365831,
                    y: 0.7326315789473683
                },
                colour: 4
            },
            {
                position: {
                    x: 2.0097325280414147,
                    y: 0.5724935289042277
                },
                colour: 4
            },
            {
                position: {
                    x: 0.7046074201898187,
                    y: 0.7306298533218291
                },
                colour: 5
            }
        ],
        flag: [
            [5, 2, 2],
            [5, 3, 3],
            [99, 99, 99]
        ]},
    configModalIsActive: false,
    serverConfiguration: {
        robot: {
            address: 'localhost',
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

export default testingState;
