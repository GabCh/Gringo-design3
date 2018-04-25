import React from 'react';
import PropTypes from 'prop-types';

const Obstacles = ({ obstacles }) => {
    const obstaclesList = obstacles.map((obstacle, i) =>
        <li key={i}><b>Obstacle #{i + 1} </b>: x:{obstacle.position.x} m, y:{obstacle.position.y} m</li>
    );
    return (
        <div>
            <h5>Obstacles</h5>
            <ul>{obstaclesList}</ul>
        </div>
    );
};

Obstacles.propTypes = {
    obstacles: PropTypes.array,
};

export default Obstacles;
