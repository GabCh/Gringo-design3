import React from 'react';
import PropTypes from 'prop-types';
import { colour } from './colour';

const NextTarget = ({ nextTarget }) => {
    const cubeSize = 50;
    const whiteCubeNumber = 5;
    const stroke = (nextTarget === whiteCubeNumber) ? 'black' : 'white';
    const strokeWidth = 2;
    const target = (
    <rect
        width={cubeSize}
        height={cubeSize}
        fill={colour[nextTarget]}
        strokeWidth={strokeWidth}
        stroke={stroke}
    />);

    return (
        <div>
            <h5>Prochain cube</h5>
            <svg>{target}</svg>
        </div>
    );
};

NextTarget.propTypes = {
    nextTarget: PropTypes.number,
};

export default NextTarget;
