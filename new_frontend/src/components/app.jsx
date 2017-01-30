import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link, IndexLink, browserHistory } from 'react-router';

import InfoModal from '../components/modal';

import { showModal } from '../actions/modal';

class App extends Component {

    constructor(props) {
        super(props);
        this.handleLoggedOutUser = this.handleLoggedOutUser.bind(this);
    }

    handleLoggedOutUser(event) {
        this.event = event;
        event.preventDefault();
        const gapi = window.gapi;
        gapi.auth2.getAuthInstance().signOut().then(() => {
            browserHistory.push('/login');
        });
    }

    render() {
        return (
            <div className="app-wrapper">
                <div className="navigation--wrapper">
                    <ul className="navigation">
                        <li><IndexLink activeClassName="is-active" to="/">
                        Home <i className="fa fa-home" /></IndexLink>
                        </li>
                        <li><Link activeClassName="is-active" to="/give-feedback">
                        Give feedback <i className="fa fa-undo" /></Link>
                        </li>
                        <li><Link activeClassName="is-active" to="/received-feedback">
                            Received feedback <i className="fa fa-thumbs-up" /></Link>
                        </li>
                        <li className="logout--link">
                            <a href="/logout" tabIndex="-1" onClick={this.handleLoggedOutUser}>
                                Logout <i className="fa fa-sign-out" />
                            </a>
                        </li>
                    </ul>
                </div>

                {this.props.children}

                <InfoModal details={this.props.modal} isOpen={this.props.modal.isOpen} {...this.props} />
            </div>
        );
    }
}

App.propTypes = {
    children: React.PropTypes.object,
    modal: React.PropTypes.object,
};

const mapStateToProps = (state) => ({
    modal: state.Modal,
});

export default connect(mapStateToProps, {showModal})(App);
