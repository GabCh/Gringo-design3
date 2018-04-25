import React from 'react';
import PropTypes from 'prop-types';
import { colour } from './colour';

const Cubes = ({ cubes }) => {
    const cubeStyle = (num) => {
        return ( {color: colour[num], fontSize: '30px'} );
    };

    const cubesList = cubes.map((cube, i) =>
        <li key={i}><b>Cube #{i + 1}</b> <span style={cubeStyle(cube.colour)}>■</span>: x:{cube.position.x} m, y:{cube.position.y} m</li>
    );
    return (
        <div>
            <h5>Cubes</h5>
            <ul>{cubesList}</ul>
        </div>
    );
};

Cubes.propTypes = {
    cubes: PropTypes.array,
};

export default Cubes;
