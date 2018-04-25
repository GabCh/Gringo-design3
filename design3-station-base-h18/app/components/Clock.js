import React, { Component } from 'react';
import PropTypes from 'prop-types';
import moment from 'moment';
import '../styles/fonts.scss';


class Clock extends Component {
    constructor(props) {
        super(props);
        this.state = {
            time: ''
        };
    }

    componentDidMount() {
        setInterval(() => {
            this.setState({
                time: this.setTime()
            });
        }, 10);
    }

    setTime() {
        const start = this.props.time.start;
        const stop = this.props.time.stop;
        const now = Date.now();
        let delta = 0;
        if (start !== 0) {
            delta += now - start;
        }
        if (stop !== 0) {
            delta += stop - now;
        }
        return moment().startOf('date').add(delta, 'ms').format('HH:mm:ss:SSS');
    }

    render() {
        return (
            <h1 style={{fontFamily: 'digital_dreamregular'}}>
                {this.state.time}
            </h1>
        );
    }
}

Clock.propTypes = {
    time: PropTypes.shape({
        start: PropTypes.number,
        stop: PropTypes.number
    })
};

export default Clock;
