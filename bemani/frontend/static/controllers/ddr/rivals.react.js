/*** @jsx React.DOM */

var valid_versions = Object.keys(window.rivals);
var pagenav = new History(valid_versions);

var rivals_view = React.createClass({

    getInitialState: function(props) {
        var profiles = Object.keys(window.rivals);
        var version = pagenav.getInitialState(profiles[profiles.length - 1]);
        return {
            rivals: window.rivals,
            players: window.players,
            profiles: profiles,
            version: version,
            term: "",
            results: {},
            searching: false,
            offset: 0,
            limit: 5,
        };
    },

    componentDidMount: function() {
        pagenav.onChange(function(version) {
            this.setState({version: version, offset: 0});
        }.bind(this));
        this.refreshRivals();
    },

    refreshRivals: function() {
        AJAX.get(
            Link.get('refresh'),
            function(response) {
                this.setState({
                    rivals: response.rivals,
                    players: response.players,
                });
				setTimeout(this.refreshRivals, 5000);
            }.bind(this)
        );
    },

    searchForPlayers: function(event) {
        this.setState({searching: true});
        AJAX.post(
            Link.get('search'),
            {
                version: this.state.version,
                term: this.state.term,
            },
            function(response) {
                this.setState({
                    results: response.results,
                    searching: false,
                });
            }.bind(this)
        );
        event.preventDefault();
    },

    addRival: function(event, userid) {
        AJAX.post(
            Link.get('addrival'),
            {
                version: this.state.version,
                userid: userid,
            },
            function(response) {
                this.setState({
                    rivals: response.rivals,
                    players: response.players,
                });
            }.bind(this)
        );
        event.preventDefault();
    },

    removeRival: function(event, userid, pos) {
        AJAX.post(
            Link.get('removerival'),
            {
                version: this.state.version,
                userid: userid,
                position: pos,
            },
            function(response) {
                this.setState({
                    rivals: response.rivals,
                    players: response.players,
                });
            }.bind(this)
        );
        event.preventDefault();
    },

    setActiveRival: function(event, userid, pos) {
        AJAX.post(
            Link.get('setactiverival'),
            {
                version: this.state.version,
                userid: userid,
                position: pos,
            },
            function(response) {
                this.setState({
                    rivals: response.rivals,
                    players: response.players,
                });
            }.bind(this)
        );
        event.preventDefault();
    },

    setInactiveRival: function(event, userid, pos) {
        AJAX.post(
            Link.get('setinactiverival'),
            {
                version: this.state.version,
                userid: userid,
                position: pos,
            },
            function(response) {
                this.setState({
                    rivals: response.rivals,
                    players: response.players,
                });
            }.bind(this)
        );
        event.preventDefault();
    },

    addRivals: function(userid) {
        if (userid == window.userid) {
            return null;
        }

        var avail = (this.state.rivals[this.state.version].length < 10);
        var current_rivals = this.state.rivals[this.state.version];
        for (var i = 0; i < current_rivals.length; i++) {
            if (current_rivals[i].userid == userid) {
                avail = false;
                break;
            }
        }

        return (
            <span>
                {avail ?
                    <Add
                        title="Add Rival"
                        onClick={function(event) {
                            this.addRival(event, userid);
                        }.bind(this)}
                    /> :
                    null
                }
            </span>
        );
    },

    render: function() {
        if (this.state.rivals[this.state.version]) {
            var rivals = [];
            var active = 0;
            this.state.rivals[this.state.version].map(function(rival) {
                rivals[rival.position] = rival;
                if (rivals[rival.position].active) {
                    active++;
                }
            }.bind(this));
            var resultlength = 0;
            Object.keys(this.state.results).map(function(userid) {
                var player = this.state.results[userid][this.state.version];
                if (player) { resultlength++; }
            }.bind(this));
            var filteredVersion = Object.values(this.state.profiles).map(function(version) {
                return Object.values(window.versions)[version-1]
            });
            var item = Object.keys(window.versions).map(function(k){
                return window.versions[k]
            })
            return (
                <div>
                    <section>
                        <p>
                            <h4>Select Version</h4>
                            <SelectVersion
                                name="version"
                                value={ filteredVersion.indexOf(item[this.state.version - 1]) }
                                versions={ filteredVersion }
                                onChange={function(event) {
                                    var version = item.indexOf(filteredVersion[event]) + 1
                                    if (this.state.editing_name) { return; }
                                    if (this.state.version == version) { return; }
                                    this.setState({
                                        version: version,
                                        new_name: this.state.player[version].name,
                                    });
                                    pagenav.navigate(version);
                                }.bind(this)}
                            />
                        </p>
                        <h3>Rivals</h3>
                    </section>
                    <section>
                        <h4>Search Rival</h4>
                        <form onSubmit={this.searchForPlayers}>
                            <div className="fields">
                                <div className="field half">
                                    <input
                                        type="text"
                                        className="inline"
                                        maxlength="9"
                                        placeholder="Name or DDR ID"
                                        value={this.state.term}
                                        onChange={function(event) {
                                            var value = event.target.value.toUpperCase();
                                            var nameRegex = /^[-&$\\.\\?!A-Z0-9 ]*$/;
                                            // Normally, names are <= 8 characters, but we allow DDR IDs here too
                                            if (value.length <= 9 && nameRegex.test(value)) {
                                                this.setState({term: value});
                                            }
                                        }.bind(this)}
                                        name="search"
                                    />
                                </div>
                                <div className="field half">
                                <input type="submit" value="search" />
                                    { this.state.searching ?
                                        <img className="loading" src={Link.get('static', 'loading-16.gif')} /> :
                                        null
                                    }
                                </div>
                            </div>
                        </form>
                        <div>
                            {resultlength > 0 ?
                                <table className="list players">
                                    <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>DDR ID</th>
                                            <th className="action"></th>
                                        </tr>
                                    </thead>
                                    <tbody>{
                                        Object.keys(this.state.results).map(function(userid, index) {
                                            if (index < this.state.offset || index >= this.state.offset + this.state.limit) {
                                                return null;
                                            }
                                            var player = this.state.results[userid][this.state.version];
                                            if (!player) { return null; }

                                            return (
                                                <tr>
                                                    <td><Rival userid={userid} player={player} /></td>
                                                    <td>{ player.extid }</td>
                                                    <td className="edit">{this.addRivals(userid)}</td>
                                                </tr>
                                            );
                                        }.bind(this))
                                    }</tbody>
                                    <tfoot>
                                        <tr>
                                            <td colSpan={2}>
                                                { this.state.offset > 0 ?
                                                    <Prev onClick={function(event) {
                                                        var page = this.state.offset - this.state.limit;
                                                        if (page < 0) { page = 0; }
                                                        this.setState({offset: page});
                                                    }.bind(this)}/> : null
                                                }
                                                { (this.state.offset + this.state.limit) < resultlength ?
                                                    <Next style={ {float: 'right'} } onClick={function(event) {
                                                        var page = this.state.offset + this.state.limit;
                                                        if (page >= resultlength) { return; }
                                                        this.setState({offset: page});
                                                    }.bind(this)}/> : null
                                                }
                                            </td>
                                        </tr>
                                    </tfoot>
                                </table> :
                                <p>No players match the specified search.</p>
                            }
                        </div>
                    </section>
                    <section>
                        <h3>Rivals</h3>
                        <table className="list players">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>DDR ID</th>
                                    <th className="action"></th>
                                </tr>
                            </thead>
                            <tbody>
                                {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map(function(rivalno) {
                                    if (!rivals[rivalno]) {
                                        return (
                                            <tr>
                                                <td colSpan={2}>
                                                    <span className="placeholder">
                                                        Empty slot
                                                    </span>
                                                </td>
                                            </tr>
                                        );
                                    }
                                    var rival = rivals[rivalno];
                                    var player = this.state.players[rival.userid][this.state.version];
                                    return (
                                        <tr>
                                            <td>
                                                <td><Rival userid={rival.userid} player={player} /></td>
                                                { rival.active ?
                                                    <div className="pill">active</div> :
                                                    null
                                                }
                                            </td>
                                            <td>{ player.extid }</td>
                                            <td className="edit">
                                                <Delete
                                                    title="Remove Rival"
                                                    onClick={function(event) {
                                                        this.removeRival(event, rival.userid, rivalno);
                                                    }.bind(this)}
                                                />
                                                { rival.active ?
                                                    <Add
                                                        title="Set Inactive"
                                                        onClick={function(event) {
                                                            this.setInactiveRival(event, rival.userid, rivalno);
                                                        }.bind(this)}
                                                    /> :
                                                    (active < window.max_active_rivals[this.state.version] ?
                                                        <Add
                                                            title="Set Active"
                                                            onClick={function(event) {
                                                                this.setActiveRival(event, rival.userid, rivalno);
                                                            }.bind(this)}
                                                        /> :
                                                        null
                                                    )
                                                }
                                            </td>
                                        </tr>
                                    );
                                }.bind(this))}
                            </tbody>
                        </table>
                    </section>
                </div>
            );
        } else {
            var item = Object.keys(window.versions).map(function(k){
                return window.versions[k]
            })
            return (
                <div>
                    <section>
                        <p>
                            <SelectVersion
                                name="version"
                                value={ item.indexOf(item[this.state.version - 1]) }
                                versions={ item }
                                onChange={function(event) {
                                    var version = item.indexOf(item[event]) + 1
                                    if (this.state.version == version) { return; }
                                    this.setState({version: version});
                                    pagenav.navigate(version);
                                }.bind(this)}
                            />
                        </p>
                    </section>
                    <section>
                        <p>You have no profile for {window.versions[this.state.version]}!</p>
                    </section>
                </div>
            );
        }
    },
});

ReactDOM.render(
    React.createElement(rivals_view, null),
    document.getElementById('content')
);
