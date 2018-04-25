import React from 'react';
import { Button, Nav, NavGroup, NavItem } from 're-bulma';
import PropTypes from 'prop-types';
import ConfigurationModal from './ConfigurationModal';
import ConnectionIndicator from './ConnectionIndicator';
import Clock from './Clock';
import { postTask } from '../services/api';
import moment from 'moment';


const Navbar = ({ configurationModalIsActive, serverConfiguration, configurationModalOnClose, submit, time }) => {
    const startCompetition = async () => {
        //eslint-disable-next-line
        console.log('started @ ' + moment().format('HH:mm:ss.SSS'));
        await postTask('start_competition', {});
    };

    return (
        <Nav>
            <ConfigurationModal
                isActive={configurationModalIsActive}
                serverConfiguration={serverConfiguration}
                onClose={configurationModalOnClose}
                submit={submit}
            />
            <NavGroup align="left">
                <NavItem>
                    <Button onClick={configurationModalOnClose}>Configuration</Button>
                    <Button color="isSuccess" onClick={startCompetition}>Start</Button>
                </NavItem>
            </NavGroup>
            <NavGroup align="center">
                <NavItem>
                    <Clock time={time}/>
                </NavItem>
            </NavGroup>
            <NavGroup align="right">
                <NavItem>
                <ConnectionIndicator
                    isConnected={serverConfiguration.robot.connected}
                    serverName={'Serveur robot'}
                />
                </NavItem>
                <NavItem>
                    <ConnectionIndicator
                        isConnected={serverConfiguration.serverImage.connected}
                        serverName={'Serveur image'}
                    />
                </NavItem>
            </NavGroup>
        </Nav>
    );
};

Navbar.propTypes = {
    configurationModalIsActive: PropTypes.bool,
    serverConfiguration: PropTypes.object,
    configurationModalOnClose: PropTypes.func,
    submit: PropTypes.func,
    time: PropTypes.shape({
        start: PropTypes.number,
        stop: PropTypes.number
    })
};

export default Navbar;
