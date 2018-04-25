import React from 'react';
import PropTypes from 'prop-types';
import Cubes from './Cubes';
import Flag from './Flag';
import Obstacles from './Obstacles';
import NextTarget from './NextTarget';
import { Content, Tile, Title } from 're-bulma';

const GameInfos = ({ infos }) => {
    let obstacles = infos.obstacles;
    let cubes = infos.cubes;
    const flag = infos.flag;
    const nextTarget = infos.nextColour;
    const style = { background: '#eee', borderRadius: '5px', padding: '10px', 'textAlign': 'left' };

    return (
        <Tile context="isParent" size="is6">
            <Tile context="isChild" style={style}>
                <Content>
                    <Title>État de la compétition</Title>
                    <Obstacles obstacles={obstacles}/>
                    <Cubes cubes={cubes} />
                    <Flag flag={flag} />
                    <NextTarget nextTarget={nextTarget} />
                </Content>
            </Tile>
        </Tile>
    );
};

GameInfos.propTypes = {
    infos: PropTypes.object
};

export default GameInfos;
