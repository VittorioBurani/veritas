import axios from 'axios';
import { DB_MODEL_NAMES } from './db-models.js';
import {
    // User API Calls:
    userDataUrl,
    passwordResetUrl,
    // JWT API Calls:
    accessTokenUrl,
    refreshTokenUrl,
    verifyTokenUrl,
    // CRUD API Calls:
    modelCRUDUrlsMethods,
} from './common-urls.js';


// Header utility:
const authHeaderHandler = (accessToken, method, multipart=false) => {
    let ret = {'Authorization': `Bearer ${accessToken}`};
    if (method !== 'get') ret['Content-Type'] = multipart ? 'multipart/form-data' : 'application/json';
    return ret
}


// User API Calls:
const userDataApiCall = (accessToken) => axios.get(userDataUrl, {headers: authHeaderHandler(accessToken, 'get')});

const passwordResetApiCall = (accessToken, new_pwd, conf_pwd) => axios.post(
    passwordResetUrl,
    {
        new_password: new_pwd,
        confirm_password: conf_pwd,
    },
    {headers: authHeaderHandler(accessToken, 'post')},
);


// JWT API Calls:
const accessTokenApiCall = (username, password) => axios.post(
    accessTokenUrl,
    {
        username: username,
        password: password,
    },
    {headers: {'Content-Type': 'application/json'}},
);

const refreshTokenApiCall = (refreshToken) => axios.post(
    refreshTokenUrl,
    {
        refresh: refreshToken
    },
    {headers: {'Content-Type': 'application/json'}},
);

const verifyTokenApiCall = (accessToken) => axios.post(
    verifyTokenUrl,
    {
        token: accessToken
    },
    {headers: {'Content-Type': 'application/json'}},
);


// DB Models API Calls:
function composeCRUDApiCall(callName, httpMethod, url) {
    if (httpMethod === 'get') {
        if (callName === 'list') {
            return (accessToken, params) => axios.get(url, {headers: authHeaderHandler(accessToken, httpMethod), params: params});
        } else {
            return (accessToken, id) => axios.get(url(id), {headers: authHeaderHandler(accessToken, httpMethod)});
        }
    }
    if (httpMethod === 'post') {
        return (accessToken, data) => axios.post(url, data, {headers: authHeaderHandler(accessToken, httpMethod)});
    }
    if (httpMethod === 'put') {
        return (accessToken, id, data) => axios.put(url(id), data, {headers: authHeaderHandler(accessToken, httpMethod)});
    }
    if (httpMethod === 'patch') {
        return (accessToken, id, data) => axios.patch(url(id), data, {headers: authHeaderHandler(accessToken, httpMethod)});
    }
    if (httpMethod === 'delete') {
        return (accessToken, id) => axios.delete(url(id), {headers: authHeaderHandler(accessToken, httpMethod)});
    }
}

const singleModelCRUDApiCalls = (modelName) => {
    let modelUrls = modelCRUDUrlsMethods(modelName);
    for (let [key, value] of Object.entries(modelUrls)) {
        if (value.methods.length === 1) {
            modelUrls[key] = composeCRUDApiCall(key, value.methods[0], value.url);
        } else {
            for (let method of value.methods) {
                modelUrls[`${method}_${key}`] = composeCRUDApiCall(key, method, value.url);
            }
        }
    }
    return modelUrls;
}

const modelsCRUDApiCalls = Object.fromEntries(DB_MODEL_NAMES.map(modelName => [modelName.replaceAll('-', '_'), singleModelCRUDApiCalls(modelName)]));


// Export all the API calls:
export {
    // User API Calls:
    userDataApiCall,
    passwordResetApiCall,
    // JWT API Calls:
    accessTokenApiCall,
    refreshTokenApiCall,
    verifyTokenApiCall,
    // CRUD API Calls:
    modelsCRUDApiCalls,
};
