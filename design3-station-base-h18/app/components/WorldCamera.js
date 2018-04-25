import React, { Component } from 'react';
import { Content, Subtitle, Tile, Title } from 're-bulma';
import PropTypes from 'prop-types';
import VisionItems from './vision/VisionItems';

const style = { background: '#eee', borderRadius: '5px', padding: '10px' };

class WorldCamera extends Component {
    constructor(props) {
        super(props);
    }

    handleConnectionState = (state) => {
        this.props.isConnected(state);
    }

    render() {
        const serverAddress = `http://${this.props.config.address}:${this.props.config.port}/video_feed`;
        return (
            <Tile context="isParent" isVertical>
                <Tile context="isChild" style={style}>
                    <Content>
                        <Title>Caméra monde</Title>
                        <Subtitle>Stream au robot</Subtitle>
                        <div style={{position: 'relative', width: 1280, height: 720}}>
                            <img
                                src={serverAddress}
                                onError={() => this.handleConnectionState(false)}
                                onLoad={() => this.handleConnectionState(true)}
                            />
                            <VisionItems vision={this.props.vision} />
                        </div>
                    </Content>
                </Tile>
            </Tile>
        );
    }
}

WorldCamera.propTypes = {
    vision: PropTypes.object,
    config: PropTypes.object,
    isConnected: PropTypes.func
};

export default WorldCamera;
