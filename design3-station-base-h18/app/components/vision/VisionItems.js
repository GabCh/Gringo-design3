import React from 'react';
import PropTypes from 'prop-types';
import { colour } from '../gameInfos/colour';
import robotSvg from './arrow-circle-left.svg';
import obstacleSvg from './times-circle.svg';

const VisionItems = ({vision}) => {
    const robotSize = 50;
    const rotation = `rotate(-${vision.robot.angle} ${vision.robot.x} ${vision.robot.y})`;
    const robotLayer = (
        <image
            x={vision.robot.x - robotSize / 2}
            y={vision.robot.y - robotSize / 2}
            transform={rotation}
            href={robotSvg}
            height={robotSize}
            width={robotSize}
        />
    );

    const cubeSize = 25;
    const cubeStyle = (cube) => {
        const whiteCubeNumber = 5;
        const stroke = (cube.colour === whiteCubeNumber) ? 'black' : 'white';
        return ({stroke: stroke, strokeWidth: '2px'});
    };
    const cubeLayers = vision.cubes.map((cube, index) =>
        <rect
            key={index}
            x={cube.x - cubeSize / 2}
            y={cube.y - cubeSize / 2}
            width={cubeSize}
            height={cubeSize}
            fill={colour[cube.colour]}
            style={cubeStyle(cube)}
        />
    );

    const obstacleSize = 50;
    const obstacleLayers = vision.obstacles.map((obstacle, index) =>
        <image
            key={index}
            x={obstacle.x - obstacleSize / 2}
            y={obstacle.y - obstacleSize / 2}
            href={obstacleSvg}
            height={obstacleSize}
            width={obstacleSize}
        />
    );

    const getPathPoints = (p) => {
        return p.map(position => position.x + ',' + position.y).join(' ');
    };

    const plannedPathLayer = (
        <polyline
            fill="none"
            stroke="blue"
            strokeWidth="3"
            points={getPathPoints(vision.path.currentPlan)}
        />
    );

    const actualPathLayer = (
        <polyline
            fill="none"
            stroke="red"
            strokeWidth="3"
            points={getPathPoints(vision.path.actual)}
        />
    );

    const otherPathLayer = vision.path.oldPlans.map((path, index) =>
        <polyline
            key={index}
            fill="none"
            stroke="grey"
            strokeWidth="1"
            points={getPathPoints(path)}
        />
    );

    const overlayStyle = {
        position: 'absolute',
        top: '0px',
        left: '0px',
        width: 1280,
        height: 720
    };

    return (
        <svg style={overlayStyle} xmlns="http://www.w3.org/2000/svg">
            {robotLayer}
            {cubeLayers}
            {obstacleLayers}
            {plannedPathLayer}
            {actualPathLayer}
            {otherPathLayer}
        </svg>
    );
};

VisionItems.propTypes = {
    vision: PropTypes.shape({
        cubes: PropTypes.arrayOf(
            PropTypes.shape({
                x: PropTypes.number,
                y: PropTypes.number,
                colour: PropTypes.number
            })
        ),
        obstacles: PropTypes.arrayOf(
            PropTypes.shape({
                x: PropTypes.number,
                y: PropTypes.number
            })
        ),
        robot: PropTypes.shape({
            x: PropTypes.number,
            y: PropTypes.number,
            angle: PropTypes.number
        }),
        path: PropTypes.shape({
            actual: PropTypes.arrayOf(
                PropTypes.shape({
                    x: PropTypes.number,
                    y: PropTypes.number
                })
            ),
            currentPlan: PropTypes.arrayOf(
                PropTypes.shape({
                    x: PropTypes.number,
                    y: PropTypes.number
                })
            ),
            oldPlans: PropTypes.arrayOf(
                PropTypes.arrayOf(
                    PropTypes.shape({
                        x: PropTypes.number,
                        y: PropTypes.number
                    })
                )
            )
        })
    })
};

export default VisionItems;
