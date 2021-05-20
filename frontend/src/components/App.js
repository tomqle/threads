import React, { Component } from "react";
import { Switch, Route, Link } from "react-router-dom";
import Login from "./Login";
import Signup from "./Signup";
import Hello from "./Hello";

class App extends Component {
  render() {
    return(
      <div className="site">
        <nav>
          <Link className={ "nav-link" } to={ "/" }>home</Link>
          <Link className={ "nav-link" } to={ "/login/" }>login</Link>
          <Link className={ "nav-link" } to={ "/signup/" }>signup</Link>
          <Link className={ "nav-link" } to={ "/hello/" }>hello</Link>
        </nav>
        <main>
          <Switch>
            <Route exact path={ "/login/" } component = { Login } />
            <Route exact path={"/signup/" } component = { Signup } />
            <Route exact path={ "/hello/" } component = { Hello } />
            <Route path={ "/" } render={ () => <div>home again</div> } />
          </Switch>
        </main>
      </div>
    );
  }
}

export default App;