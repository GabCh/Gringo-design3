import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Content, Subtitle, Tile, Title } from 're-bulma';


class Logging extends Component {
    constructor(props) {
        super(props);
        this.state = {
            event: 'logging',
            loggingMessages: []
        };
    }

    componentDidMount() {
        this.props.socket.on(this.state.event, data => {
            this.setState(prevState =>({
                loggingMessages: [...prevState.loggingMessages, data]}));
        });
    }

    render() {
        const style = { background: '#eee', borderRadius: '5px', padding: '10px', 'textAlign': 'center' };
        const messages = this.state.loggingMessages.map(
            (message, i) => (<p key={i}>{message}</p>)
        );

        return(
            <Tile isVertical size="is4" context="isParent">
                <Tile context="isChild" style={style}>
                    <Content>
                        <Title>Logging</Title>
                        <Subtitle>Pour débugger</Subtitle>
                        {messages}
                    </Content>
                </Tile>
            </Tile>
        );
    }
}

Logging.propTypes = {
    socket: PropTypes.object
};

export default Logging;
