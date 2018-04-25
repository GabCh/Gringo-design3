import React, { Component } from 'react';
import { Button, Content, Subtitle, Tile, Title } from 're-bulma';
import { postTask, post } from '../services/api';

const style = { background: '#eee', borderRadius: '5px', padding: '10px', 'textAlign': 'center' };

class Controles extends Component {
    constructor(props) {
        super(props);
    }

    handleClick = (taskType, parameter) => {
        postTask(taskType, parameter);
    }
    render() {
        return (
            <Tile context="isParent">
                <Tile context="isChild" style={style}>
                    <Content>
                        <Title>Contrôles</Title>
                        <Subtitle>Contrôles du robot</Subtitle>
                            <div>
                                <Button onClick={() => this.handleClick('move', {'direction': 'left', 'distance': 10})}>◀</Button>
                                <Button onClick={() => this.handleClick('move_forward', {'distance': 10})}>▲</Button>
                                <Button onClick={() => this.handleClick('move', {'direction': 'backward', 'distance': 10})}>▼</Button>
                                <Button onClick={() => this.handleClick('move', {'direction': 'right', 'distance': 10})}>▶</Button>
                                <Button onClick={() => this.handleClick('rotate', {'angle': 90})}>⥀</Button>
                                <Button onClick={() => this.handleClick('rotate', {'angle': -90})}>⥁</Button>
                                <Button onClick={() => post('/imageRequest', '')}>Simuler image</Button>
                            </div>
                    </Content>
                </Tile>
            </Tile>
        );
    }
}


export default Controles;
