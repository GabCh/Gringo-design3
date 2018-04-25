import openSocket  from 'socket.io-client';
import axios from 'axios';

let baseUrl;

const setBaseUrl = (url) => {
    baseUrl = url;
};

const connectSocket = (serverAdress) => {
    return openSocket(serverAdress);
};

const disconnectSocket = (socket) => {
    socket.disconnect();
};

const setRobotServerDefaultsSettings = () => {
    axios.defaults.headers.post['Content-Type'] = 'application/json';
    axios.defaults.headers = {
        'Access-Control-Allow-Origin': '*',
        'token': '07624953d862ede4a6264c42b3e81051'
    };
};


const post = async (route, body) => {
    let response;
    try {
        response = await axios.post(baseUrl + route, JSON.stringify(body));
    } catch(err) {
        //eslint-disable-next-line
        console.error(err)
    }
    return response;
};

const get = async (route) => {
    let response;
    try {
        response = await axios.get(baseUrl + route);
    } catch (err) {
        //eslint-disable-next-line
        console.error(err);
    }
    return response;
};

const postTask = async (taskName, params) => {
    const body = {
        tasks: [{
            task_name: taskName,
            params: params
        }]
    };

    return post('/tasks', body);
};

export { postTask, post, setRobotServerDefaultsSettings, get, connectSocket, disconnectSocket, setBaseUrl };

