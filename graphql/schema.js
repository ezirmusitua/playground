const { GraphQLObjectType, GraphQLSchema, GraphQLInt, GraphQLString, GraphQLList } = require('graphql');

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
    })
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
            }
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

module.exports = {DemoSchema};