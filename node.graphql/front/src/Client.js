import {GraphQLClient} from 'graphql-request';

const BASE_SERVER_URL = 'http://localhost:3002/graphql';

class Client {
    static Instance;
    static options = {};
    static base = '';

    constructor (base, options = {}) {
        if (!Client.Instance) {
            Client.base = base;
            Client.options = options;
            if (!Client.options.headers) {
                Client.options.headers = new Headers();
            }
            if (!(Client.options.headers instanceof Headers)) {
                Client.options.headers = new Headers(Client.options.headers);
            }
            Client.options.headers.set('Content-Type', 'application/graphql');
            Client.options.method = 'Post';
            Client.Instance = this;
        }
        return Client.Instance;
    }

    request (resource = '', query) {
        return fetch(Client.base + resource, Object.assign(
          {}, Client.options, { body: query }),
        )
    }
}

function toFilter(filter) {
    return Object.keys(filter).reduce((res, key) => {
        res += (key + ': ' + filter[key]);
        return res;
    }, '')
}

function toField(field) {
    return field.reduce((res, key) => {
        res += (key + ', ');
        return res;
    }, '').slice(0, -1);
}

export function counter () {
    return 'count';
}

export function user(field, filter) {
    let query = 'user ';
    if (filter) {
        query += '(' + toFilter(filter) + ') { ' + toField(field) + ' }';
    } else {
        query += '{ ' + toField(field) + ' }'; 
    }
    console.log(query);
    return query;
}

export function updateCount(field) {
    
}

export function query (...args) {
    return `query { ${args} }`;
}

export function mutation (...args) {
    return `mutation { ${args} }`;
}

export const client = new Client('http://127.0.0.1:3002/graphql');
