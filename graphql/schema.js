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
                resolve: function () {
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
                resolve: function () {
                    count += 1;
                    return count;
                },
            },
        },
    }),
});

module.exports = { DemoSchema };