import React, {Component} from 'react';
import './App.css';

class Counter extends Component {
    componentWillMount () {
        const { count } = this.props;
        this.setState({ count: count || 0 })
    }

    updateCount () {
        // TODO: call update count API, and use return value as new state.count
    }

    syncCount () {
        // TODO: Sync count with get count API
    }

    render () {
        return (<section>
            <h2>Counter</h2>
            <div>
                <p>Current count is: {this.state.count}</p>
                <button>Sync</button>
            </div>
            <form>
                <fieldset>
                    <label>Input new count: </label>
                    <input type="number"/>
                </fieldset>
                <button>Update</button>
            </form>
        </section>)
    }
}

class User extends Component {
    componentWillMount () {

    }

    render () {
        return (<section>
            <h2>Users</h2>
            <table>
                <caption>Current Users</caption>
                <tr>
                    <th>Name</th>
                    <th>Caught Count</th>
                    <th>Create</th>
                </tr>
                <tr>
                    <td>Jferroal</td>
                    <td>3</td>
                    <td>0</td>
                </tr>
            </table>
            <form>
                <legend>Create New User</legend>
                <fieldset>
                    <label>User Name</label>
                    <input/>
                </fieldset>
                <button>Create</button>
            </form>
        </section>)
    }
}

class Pokemon extends Component {
    componentWillMount () {
        `Pokédex data
National №	001
Type	GRASS POISON
Species	Seed Pokémon
Height	2′4″ (0.71m)
Weight	15.2 lbs (6.9 kg)
Abilities	Overgrow
Chlorophyll (hidden ability)
Local №	001 (Red/Blue/Yellow/FireRed/LeafGreen)
226 (Gold/Silver/Crystal)
231 (HeartGold/SoulSilver)
080 (X/Y)
Japanese	Fushigidane`
    }

    render () {
        return (<section>
            <h2>Pokemon</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Stage</th>
                    <th>Species</th>
                </tr>
                <tr>
                    <td>Fushigidane</td>
                    <td>100</td>
                    <td>10</td>
                    <td>Seed Pokemon</td>
                </tr>
            </table>
        </section>)
    }
}


class App extends Component {
    render () {
        return (<div className="App">
            <Counter count={10}/>
            <hr/>
            <User/>
            <hr/>
            <Pokemon/>
        </div>);
    }
}

export default App;
