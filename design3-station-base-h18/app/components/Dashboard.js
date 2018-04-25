import React, { Component } from 'react';
import { Tile } from 're-bulma';
import WorldCamera from './WorldCamera';
import GameInfos from './gameInfos/GameInfos';
import Controles from './Controles';
import Logging from './Logging';
import NavBar from './Navbar';
import initialState from '../state/initialState';
import { connectSocket, setRobotServerDefaultsSettings, disconnectSocket, setBaseUrl, get } from '../services/api';


class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = initialState;
        this.socket = this.initializeSocket();
        setRobotServerDefaultsSettings();
        this.setRobotBaseUrl();
    }

    componentDidMount() {
        this.socket.on('connect', () => {
            const serverConfigurationState = this.state.serverConfiguration;
            serverConfigurationState.robot.connected = true;
            this.setState({serverConfiguration: serverConfigurationState});
        });
        this.socket.on('disconnect', () => {
            const serverConfigurationState = this.state.serverConfiguration;
            serverConfigurationState.robot.connected = false;
            this.setState({serverConfiguration: serverConfigurationState});
        });
        this.updateGameState();
    }

    updateGameState = () => {
        setInterval(async () => {
            const req = await get('/status');
            const gameState = req ? req.data : this.state.gameState;
            this.setState({ gameState: gameState });
        }, 1000);
    }

    setRobotBaseUrl = () => {
        const address = this.state.serverConfiguration.robot.address;
        const port = this.state.serverConfiguration.robot.port;
        setBaseUrl(`http://${address}:${port}`);
    }

    initializeSocket = () => {
        const address = this.state.serverConfiguration.robot.address;
        const port = this.state.serverConfiguration.robot.port;
        return connectSocket(`http://${address}:${port}`);
    }

    toggleModal = () => {
        this.setState({configModalIsActive: !this.state.configModalIsActive});
    }

    changeServerConfiguration = (robotServerAddress, robotServerPort, serverImageAddress, serverImagePort) => {
        const serverConfigurationState = this.state.serverConfiguration;
        serverConfigurationState.robot.address = robotServerAddress;
        serverConfigurationState.robot.port = robotServerPort;
        serverConfigurationState.serverImage.address = serverImageAddress;
        serverConfigurationState.serverImage.port = serverImagePort;
        this.setState({serverConfiguration: serverConfigurationState});
        this.toggleModal();
        disconnectSocket(this.socket);
        this.setRobotBaseUrl();
        this.initializeSocket();
    }

    setCameraServerState = (serverState) => {
        const serverConfigurationState = this.state.serverConfiguration;
        serverConfigurationState.serverImage.connected = serverState;
        this.setState({serverConfiguration: serverConfigurationState});
    }

    render() {
        return(
            <div>
                <NavBar
                    configurationModalIsActive={this.state.configModalIsActive}
                    serverConfiguration={this.state.serverConfiguration}
                    configurationModalOnClose={this.toggleModal}
                    submit={this.changeServerConfiguration}
                    time={this.state.gameState.time}
                />
                <Tile context="isAncestor">
                    <WorldCamera
                        vision={this.state.gameState.vision}
                        config={this.state.serverConfiguration.serverImage}
                        isConnected={this.setCameraServerState}
                    />
                </Tile>
                <Tile context="isAncestor">
                    <GameInfos infos={this.state.gameState} />
                    <Controles />
                    <Logging socket={this.socket} />
                </Tile>
            </div>
        );
    }
}

export default Dashboard;
