const { GraphQLObjectType, GraphQLSchema, GraphQLInt, GraphQLString, GraphQLList, GraphQLNonNull } = require('graphql');

const MockUsers = {
    'jferroal': { name: 'jferroal', caught: [], created: 0 },
};

let count = 0;

const PokemonType = new GraphQLObjectType({
    name: 'Pokemon',
    description: 'A Pokemon',
    fields: () => ({
        name: {
            type: GraphQLString,
            description: 'Name of pokemon',
        },
        type: {
            type: GraphQLInt,
            description: 'Type of pokemon',
        },
        stage: {
            type: GraphQLInt,
            description: 'Level of pokemon',
        },
        species: {
            type: GraphQLString,
            description: 'Species of pokemon',
        },
    }),
});


const UserType = new GraphQLObjectType({
    name: 'User',
    description: 'An User',
    fields: () => ({
        name: {
            type: GraphQLString,
            description: 'Name of user',
        },
        caught: {
            type: new GraphQLList(GraphQLString),
            description: 'The pokemon has been caught by current user',
        },
        created: {
            type: GraphQLInt,
            description: 'when the create',
        },
    }),
});


const DemoSchema = new GraphQLSchema({
    query: new GraphQLObjectType({
        name: 'RootQueryType',
        fields: {
            count: {
                type: GraphQLInt,
                description: 'Fetch the count',
                resolve: () => {
                    return count;
                },
            },
            pokemon: {
                type: new GraphQLList(PokemonType),
                resolve: () => [],
            },
            user: {
                type: UserType,
                args: {
                    name: {
                        description: 'Name of user',
                        type: new GraphQLNonNull(GraphQLString),
                    },
                },
                resolve: (root, { name }) => {
                    return Promise.resolve(MockUsers[ name ]);
                },
            },
        },
    }),
    mutation: new GraphQLObjectType({
        name: 'RootMutationType',
        fields: {
            updateCount: {
                type: GraphQLInt,
                description: 'Updates the count',
                resolve: () => {
                    count += 1;
                    return count;
                },
            },
            upsertUser: {
                type: UserType,
                args: {
                    name: {
                        description: 'name of the user',
                        type: new GraphQLNonNull(GraphQLString),
                    },
                },
                resolve: (obj, {name}) => {
                    let user = MockUsers[name];
                    if (!user) {
                        user = MockUsers[name] = {name, caught: [], created: count};
                    }
                    return Promise.resolve(user);
                }
            },
            caughtPokemon: {
                type: UserType,
                args: {
                    name: {
                        description: 'name of user',
                        type: new GraphQLNonNull(GraphQLString),
                    },
                    pokemon: {
                        description: 'name of pokemon',
                        type: new GraphQLNonNull(GraphQLString),
                    }
                },
                resolve: (obj, {name, pokemon}) => {
                    const user = MockUsers[name];
                    // TODO: 抛出异常?
                    if (!user) return Promise.resolve();
                    (user.caught.indexOf(pokemon) < 0) && user.caught.push(pokemon);
                    return user;
                }
            }
        },
    }),
});

module.exports = { DemoSchema };