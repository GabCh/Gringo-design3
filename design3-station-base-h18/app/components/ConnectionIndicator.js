import React from 'react';
import PropTypes from 'prop-types';

const ConnectionIndicator = ({ isConnected, serverName }) => {
    const indicatorColor = isConnected ? '#00D100' : '#FF0000';
    const style = {fill: indicatorColor, display: 'inline-block', marginRight: '5px'};
    return (
        <span>
            <svg width="10" height="10" viewBox="0 0 10 10" style={style}>
                <circle cx="5" cy="5" r="5"/>
            </svg>
            <p style={{display: 'inline-block'}}>{serverName}</p>
        </span>
    );
};

ConnectionIndicator.propTypes = {
    isConnected: PropTypes.bool,
    serverName: PropTypes.string
};

export default ConnectionIndicator;
