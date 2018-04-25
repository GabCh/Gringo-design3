import React from 'react';
import PropTypes from 'prop-types';
import { colour } from './colour';

const Flag = ({ flag }) => {
    const cubeStyle = (num) => {
        return ( {fill: colour[num], stroke: 'black'} );
    };
    const SIZE = 50;

    const flagObj = flag.visual.map((cubeRow, i) =>
        cubeRow.map((cube, j) =>
            <rect width={SIZE} height={SIZE} x={SIZE * j} y={SIZE * i} style={cubeStyle(cubeRow[j])} />
        )
    );
    return (
        <div>
            <h5>Drapeau du {flag.name}, #{flag.number}</h5>
            <svg>{flagObj}</svg>
        </div>
    );
};

Flag.propTypes = {
    flag: PropTypes.object,
};

export default Flag;
