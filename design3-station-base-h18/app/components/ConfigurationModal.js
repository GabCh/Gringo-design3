import React, { Component } from 'react';
import { Content, Modal, Button, Label } from 're-bulma';
import PropTypes from 'prop-types';

class ConfigurationModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            robotServerAddress: this.props.serverConfiguration.robot.address,
            robotServerPort: this.props.serverConfiguration.robot.port,
            serverImageAddress: this.props.serverConfiguration.serverImage.address,
            serverImagePort: this.props.serverConfiguration.serverImage.port
        };
    }

    setRobotServerAddress = (e) => {
        this.setState({
            robotServerAddress: e.target.value
        });
    }

    setRobotServerPort = (e) => {
        this.setState({
            robotServerPort: e.target.value
        });
    }

    setServerImageAddress = (e) => {
        this.setState({
            serverImageAddress: e.target.value
        });
    }

    setServerImagePort = (e) => {
        this.setState({
            serverImagePort: e.target.value
        });
    }

    handleSubmit = (robotServerAddress, robotServerPort, serverImageAddress, serverImagePort) => {
        this.props.submit(robotServerAddress, robotServerPort, serverImageAddress, serverImagePort);
    }

    resetState = () => {
        this.setState({
            robotServerAddress: this.props.serverConfiguration.robot.address,
            robotServerPort: this.props.serverConfiguration.robot.port,
            serverImageAddress: this.props.serverConfiguration.serverImage.address,
            serverImagePort: this.props.serverConfiguration.serverImage.port
        });
    }

    handleClose = () => {
        this.resetState();
        this.props.onClose();
    }

    render() {
        const footerContent = (
            <div style={{ padding: '20px'}} >
                <Button
                    color="isPrimary"
                    onClick={() => this.handleSubmit(this.state.robotServerAddress, this.state.robotServerPort, this.state.serverImageAddress, this.state.serverImagePort)}
                >
                    Enregistrer
                </Button>
            </div>
        );

        return (
            <Modal
                type="card"
                headerContent="Configuration"
                footerContent={footerContent}
                isActive={this.props.isActive}
                onCloseRequest={() => this.handleClose()}
            >
                <Content>
                    <Label>Adresse du serveur du robot</Label>
                    <input
                        type="text"
                        autoFocus
                        value={this.state.robotServerAddress}
                        className="__re-bulma_input"
                        onChange={this.setRobotServerAddress}
                    />
                    <span className="__re-bulma_help">En local: localhost ou sur le robot: design-whitecat.local</span>

                    <Label>Port du serveur du robot</Label>
                    <input
                        type="text"
                        autoFocus
                        value={this.state.robotServerPort}
                        className="__re-bulma_input"
                        onChange={this.setRobotServerPort}
                    />

                    <Label>Adresse du serveur d'image</Label>
                    <input
                        type="text"
                        autoFocus
                        value={this.state.serverImageAddress}
                        className="__re-bulma_input"
                        onChange={this.setServerImageAddress}
                    />

                    <Label>Port du serveur d'image</Label>
                    <input
                        type="text"
                        autoFocus
                        value={this.state.serverImagePort}
                        className="__re-bulma_input"
                        onChange={this.setServerImagePort}
                    />

                </Content>
            </Modal>
        );
    }
}


ConfigurationModal.propTypes = {
    isActive: PropTypes.bool,
    serverConfiguration: PropTypes.object,
    onClose: PropTypes.func.isRequired,
    submit: PropTypes.func.isRequired
};

export default ConfigurationModal;
